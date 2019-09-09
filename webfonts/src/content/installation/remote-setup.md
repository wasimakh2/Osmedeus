---
title: "Remote Setup"
date: 2019-08-08T21:30:31+07:00
draft: false
weight: 2
---

### Setup Flask API server on remote server.
Allow Web UI access from remote but do not allow run command directly on it.

```
python3 core/app.py -b 0.0.0.0 -p 5000
```
or 

Because this API allows executing command on your server so by default it only allows execute command from localhost so if you specify `--remote` It's will remove local protection on that API.
```
python3 core/app.py -b 0.0.0.0 -p 5000 --remote
```

---
### Web UI connect

![ui-login](https://user-images.githubusercontent.com/23289085/62712052-50481100-ba24-11e9-893a-1ec1c731951b.png?classes=border,shadow)

Connect your UI to API Server.

---

### Running Osmedeus
**_Protips_**: `--auth="username:password"` using this option for custom credentials. 

#### Access the remote server and do screen or tmux then run 

```
./osmedeus.py -t example.com --client
```
or 
```
./osmedeus.py -t example.com --client --remote https://yourserver.com:5000
```

***

### Beautify Postman dashboard

Full API Endpoint will be updated [here](https://documenter.getpostman.com/view/7482578/S1a626XR?version=latest).

![Postman Dashboard](https://user-images.githubusercontent.com/23289085/60317344-d0e10f80-9998-11e9-9976-77116ca6e76a.png?classes=border,shadow)


**_Note that **duckduckgo.com** is an example target, replace it depending on your target._**


#### API Config
You gonna need JWT token to reach out the endpoints. But first, we gonna need to define the credentials to verify the authentication process.
So check out the login [API](https://documenter.getpostman.com/view/7482578/S1a626XR?version=latest#60fee8fe-4830-4ab5-86af-909b7964305b) first 


*** 

### Security concern
**_Protips_**: you can access the UI or even the API safe by using ssh forwarding using this command (make sure you're enable `GatewayPorts yes` in your `/etc/ssh/sshd_config`)
```
ssh -L 5000:localhost:5000 root@your_remote_server
```

Because this API allows executing command on your server so `@local_only` and `@jwt_required` decorators on core endpoints are really important.

If you wanna run it remote just remove `@local_only` decorators or run the server with `--remote` options but make sure you know that are you doing.

### Others best practice

Make sure change `JWT_SECRET_KEY` and the CORS origin on `core/app.py` to where you host the UI.

```
#just for testing whitelist your domain if you wanna run this server remotely
cors = CORS(app, resources={r"/*": {"origins": "*"}})

...

# setup jwt secret, make sure you change this!
app.config['JWT_SECRET_KEY'] = '-----BEGIN RSA PRIVATE KEY-----' # go ahead, spider

```

#### Create your own certificate.
Navigate to `core/certs` delete cert.pem and key.pem in this folder and create your own cert by this command below.

```
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
```