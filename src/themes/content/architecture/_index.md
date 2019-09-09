---
title: "Architecture"
date: 2019-08-08T21:13:44+07:00
draft: true
---

Osmedeus basically split in two main part, Flask API server and python client.

### The architecture
Normally, Osmedeus will run the subprocess `python3 core/app.py run` to start API server and continue as a python client. 

But if you want to run it separately for remote purpose (_make sure you know what are you doing by config the `remote_api` in your `config.conf` file_) then just run 

```
python3 core/app.py -b 0.0.0.0 -p 5000
```
which is bind the server on all interface on local machine and port 5000.

Highly recommend check out [Remote-Setup](/installation/remote-setup/) for security concerns.
****

and run Osmedeus with --client options

```
./osmedeus -t example.com --client
```

------

### Flask API server
Require `flask flask_restful flask_jwt flask_cors flask_jwt_extended` to run so make sure you installed those libraries before run 

`python3 core/app.py` 

Check out REST-API for all [endpoints](https://documenter.getpostman.com/view/7482578/S1a626XR?version=latest).

------

### Python client
Require `requests` library to send request to the API server.

Basically, this client will do the logic, parsing and storing the result in the workspace by running run the [collection](https://github.com/j3ssie/Osmedeus/blob/master/CREDITS.md) of awesome tools against the target.

The order of the logic is described in `core/routine.py` file.


