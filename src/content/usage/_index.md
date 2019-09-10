---
title: "Usage"
date: 2019-07-31T13:44:32+07:00
draft: false
weight: 3
---

If you have no idea what are you doing just type the command below or check out the [Advanced Usage](/advanced/)

```bash
./osmedeus.py -t example.com
```

## Example Commands

``` bash
# normal routine
./osmedeus.py -t example.com

# normal routine but slow speed on all module
./osmedeus.py -t example.com --slow 'all'

# direct mode examples
./osmedeus.py -m portscan -i "1.2.3.4/24"

./osmedeus.py -m portscan -I list_of_targets.txt -t result_folder

./osmedeus.py -m "portscan,vulnscan" -i "1.2.3.4/24" -t result_folder
./osmedeus.py -m "git" -i 'repo:https://github.com/foo/bar'
./osmedeus.py -m "git" -i 'user:sample'

# report mode
./osemdeus.py -t example.com --report list
./osemdeus.py -t example.com --report sum
./osemdeus.py -t example.com --report short
./osemdeus.py -t example.com --report full
```

## More options

```bash
Basic Usage
===========
python3 osmedeus.py -t <your_target>
python3 osmedeus.py -T <list_of_targets>
python3 osmedeus.py -m <module> [-i <input>|-I <input_file>] [-t workspace_name]
python3 osmedeus.py --report <mode> -t <workspace> [-m <module>]

Advanced Usage
==============
[*] List all module
python3 osmedeus.py -M

[*] List all report mode
python3 osmedeus.py --report help

[*] Running with specific module
python3 osmedeus.py -t <result_folder> -m <module_name> -i <your_target>

[*] Example command
python3 osmedeus.py -m subdomain -t example.com
python3 osmedeus.py -t example.com --slow "subdomain"
python3 osmedeus.py -t sample2 -m vuln -i hosts.txt
python3 osmedeus.py -t sample2 -m dirb -i /tmp/list_of_hosts.txt

Remote Options
==============
--remote REMOTE       Remote address for API, (default: https://127.0.0.1:5000)
--auth AUTH           Specify authentication e.g: --auth="username:password"
                      See your config file for more detail (default: core/config.conf)

--client              just run client stuff in case you ran the flask server before

More options
==============
--update              Update lastest from git

-c CONFIG, --config CONFIG
                      Specify config file (default: core/config.conf)

-w WORKSPACE, --workspace WORKSPACE
                      Custom workspace folder

-f, --force           force to run the module again if output exists
-s, --slow  "all"
                      All module running as slow mode
-s, --slow  "subdomain"
                      Only running slow mode in subdomain module

--debug               Just for debug purpose


```