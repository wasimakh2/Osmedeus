---
title: "Understand a Module"
date: 2019-09-09T13:33:20+07:00
draft: false
weight: 2
---

### Skeleton module

Skeleton module define a main logic for each module. All other modules should inheritance from this.

```python

class Skeleton(object):

    # prepare and parsing input for current module
    def initial(self):

    # check if the module already done or not
    def resume(self):

    # get command for this module base on mode from workflow
    def gen_commands(self):


    # split commands in 3 parts then run it first, mid, post
    def routine(self): #

    # run pre method, command and post method for each module
    def really_routine(self, commands):

    #  run methods in current class
    def sub_routine(self, commands, kind='post'):

    # loop through pre-defined commands and run it
    def run(self, commands):

    # some task after done the routine
    def conclude(self):

```

### Routine from workflow

Default workflow on `lib/workflow/` for each mode. Each module is each `Class` on that.

For example `Class PortScan:` in **direct** mode will place in `lib/workflow/direct_list.py` 

Detail about workflow. all string start with `$ANYTHING` will be replaced at runtime with config.

``` python

class PortScan:
    # result file to push Reports table
    reports = [
        {
            "path": "$WORKSPACE/portscan/final-$OUTPUT.html",
            "type": "html",
            "note": "final",
        },
        {
            "path": "$WORKSPACE/portscan/screenshot-$OUTPUT.html",
            "type": "html",
            "note": "final",
        },
        {
            "path": "$WORKSPACE/portscan/$OUTPUT-masscan.csv",
            "type": "bash",
            "note": "final",
        },
        {
            "path": "$WORKSPACE/portscan/screenshot/$OUTPUT-raw-gowitness.html",
            "type": "html",
            "note": "",
        },
    ]
    logs = []
    # real comand gonna executed
    # routine for module: waiting:first --> no waiting --> waiting:last
    # routine for each command: pre_run --> cmd --> post_run
    commands = {
        'general': [
            {
                "banner": "Masscan 65535 ports",
                "cmd": "$ALIAS_PATH/portscan -i $TARGET -o '$WORKSPACE/portscan/$OUTPUT' -s '$WORKSPACE/portscan/summary.txt' -p '$PLUGINS_PATH'",
                "output_path": "$WORKSPACE/portscan/$OUTPUT.xml",
                "std_path": "",
                "waiting": "first",
            },
            {
                "requirement": "$WORKSPACE/portscan/$OUTPUT.csv", # file to check before run the command
                "banner": "CSV beautify",
                "cmd": "cat $WORKSPACE/portscan/$OUTPUT.csv | csvlook --no-inference | tee $WORKSPACE/portscan/beautify-$OUTPUT.txt",
                "output_path": "$WORKSPACE/portscan/beautify-$OUTPUT.txt",
                "std_path": "",
                "pre_run": "update_ports",
                "cleaned_output": "$WORKSPACE/portscan/formatted-$OUTPUT.txt",
            },
            {
                "requirement": "$WORKSPACE/portscan/$OUTPUT.csv",
                "banner": "Screenshot on ports found",
                "cmd": "$GO_PATH/gowitness file -s $WORKSPACE/portscan/scheme-$OUTPUT.txt -t 30 --log-level fatal --destination $WORKSPACE/portscan/screenshot/raw-gowitness/ --db $WORKSPACE/portscan/screenshot/gowitness.db",
                "output_path": "$WORKSPACE/portscan/screenshot/gowitness.db",
                "std_path": "",
                "post_run": "clean_gowitness",
                "pre_run": "get_scheme",
                "cleaned_output": "$WORKSPACE/portscan/screenshot-$OUTPUT.html",
                "waiting": "last",
            },
            
        ],
    }
```