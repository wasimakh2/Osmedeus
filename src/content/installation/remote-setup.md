---
title: "Remote Setup"
date: 2019-08-08T21:30:31+07:00
draft: false
weight: 2
---

### Setup REST API server on remote server
Open your **tmux** or what ever and run the API server persistence by using this command

``` bash
python3 server/manage.py runserver
```
or 

``` bash
python3 server/manage.py runserver 0.0.0.0:8000
```
if you want to bind this server on other IP and port.

### Run osmedeus client
Open your **tmux** or what ever and run on that machine too (recommendation)

``` bash
./osmedeus -t example.com
```

or if you really want to run a client on your server just do

``` bash
./osmedeus -t example.com --remote http://your_remote_ip:port
```

{{% notice tip %}}
Check out [sercurity concern](/Osmedeus/mics/security-concern/) to protect your server.
{{% /notice %}}

