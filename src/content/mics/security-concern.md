---
title: "Security Concern"
date: 2019-09-09T11:43:55+07:00
draft: false
---

### Overview

Because main feature of Osmedeus is allow execute command on your system so make sure you secure it.
If you run default config Osmedeus only can access via your localhost.

### Turn off Debug mode in `server/rest/settings.py`

```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
```

### Access remote via SSH tunnel (easiest way)

You can also achieve remote access in safe method using SSH.

```bash
ssh -L 8000:localhost:8000 root@your_remote_server
```

make sure you're enable `GatewayPorts yes` in your `/etc/ssh/sshd_config` on remote server.

### Change your secret key in `server/rest/settings.py`
Use same **SECRET_KEY** on the github repo gonna let someone create valid token and login to your server.

```python
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your_key_here'

```

### Running on SSL via nginx
If you running Osmedeus server on remote make sure you have SSL setup otherwise you gonna lose your JWT in untrusted network and can defenily lead to a Remote Code Execution on your server.

Read this great [article](https://simpleisbetterthancomplex.com/tutorial/2016/05/11/how-to-setup-ssl-certificate-on-nginx-for-django-application.html) for setup.