import os
import json
from flask import Flask, jsonify, render_template, request
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import jwt_required
from .decorators import local_only
import utils, slack, execute
current_path = os.path.dirname(os.path.realpath(__file__))

'''
Executing abritary command so it's a feature not an RCE bug :D
'''


class Cmd(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('cmd',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    parser.add_argument('output_path',
                        type=str,
                        required=False,
                        help="This field cannot be left blank!"
                        )

    parser.add_argument('std_path',
                        type=str,
                        required=False
                        )

    parser.add_argument('module',
                        type=str,
                        required=True
                        )

    parser.add_argument('nolog',
                        type=str,
                        required=False,
                        default="False"
                        )

    # just return list of workspaces
    def __init__(self, **kwargs):
        self.options = utils.reading_json(current_path + '/storages/options.json')

    @jwt_required
    @local_only
    def post(self):
        data = Cmd.parser.parse_args()
        cmd = data['cmd']
        std_path = data['std_path']
        output_path = data['output_path']
        module = data['module']
        nolog = data['nolog']

        activity = {
            'cmd': cmd,
            'std_path': std_path,
            'output_path': output_path,
            'status': 'Running'
        }

        if nolog == 'False':
            activities = utils.reading_json(current_path + '/storages/activities.json')
            if activities.get(module):
                activities[module].append(activity)
            else:
                activities[module] = [activity]
            
            utils.just_write(current_path + '/storages/activities.json',
                            activities, is_json=True)
            slack.slack_noti('log', self.options, mess={
                'title':  "{0} | {1} | Execute".format(self.options['TARGET'], module),
                'content': '```{0}```'.format(cmd),
            })

        utils.print_info("Execute: {0} ".format(cmd))


        stdout = execute.run(cmd)
        # just ignore for testing purpose
        # stdout = "<< stdoutput >> << {0} >>".format(cmd)
        utils.check_output(output_path)

        if nolog == 'False':
            # change status of log
            activities = utils.reading_json(current_path + '/storages/activities.json')
            for item in activities[module]:
                if item['cmd'] == cmd:
                    if stdout is None:
                        item['status'] = 'Error'
                    else:
                        item['status'] = 'Done'
                        try:
                            if std_path != '':
                                utils.just_write(std_path, stdout)
                                slack.slack_file('std', self.options, mess={
                                    'title':  "{0} | {1} | std".format(self.options['TARGET'], module),
                                    'filename': '{0}'.format(std_path),
                                })
                            if output_path != '':
                                slack.slack_file('verbose-report', self.options, mess={
                                    'channel': self.options['VERBOSE_REPORT_CHANNEL'],
                                    'filename': output_path
                                })
                        except:
                            pass

            utils.just_write(current_path + '/storages/activities.json', activities, is_json=True)

        return jsonify(status="200", output_path=output_path)
