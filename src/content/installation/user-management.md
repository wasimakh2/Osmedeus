---
title: "User Management"
date: 2019-09-09T11:43:38+07:00
draft: false
---

### Guide

Osmedeus use [Django authentication system](https://docs.djangoproject.com/en/2.2/topics/auth/default/) to mange users and create token.

You directly create new user by using this command below.

```bash
python3 server/manage.py createsuperuser
```

These user also used to login on Web UI.