---
title: "Architecture"
date: 2019-08-08T21:13:44+07:00
draft: false
---

Osmedeus basically split in two main part, Django API server and python client.

### The architecture
Normally, Osmedeus will run the subprocess `python3 server/manage.py runserver` to start API server and continue as a python client. 

But if you want to run it separately for remote purpose just run 

```
python3 server/manage.py runserver 0.0.0.0:8000
```

which is bind the server on all interface on local machine and port 8000.

Highly recommend check out [Remote-Setup](/installation/remote-setup/) for security concerns.

****

and run Osmedeus with --client options

```
./osmedeus -t example.com --client
```

------

### Django API server
Require `Django, djangorestframework` to run so make sure you installed those libraries before run 

`python3 server/manage.py runserver 0.0.0.0:8000` 

Check out REST-API for all [endpoints](https://documenter.getpostman.com/view/7482578/SVmpWgnE).

------


### Python client
Require `requests` library to send request to the API server.

Basically, this client will do the logic, parsing and storing the result in the workspace by running run the [collection](https://github.com/j3ssie/Osmedeus/blob/master/CREDITS.md) of awesome tools against the target.

The order of the logic is described in `Osmedeus/lib/workflow/` file.
