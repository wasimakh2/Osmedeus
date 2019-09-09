---
title: "Token setup"
date: 2019-08-08T21:51:02+07:00
draft: false
weight: 3
---


## Create Slack token

![slack-1](screenshots/slack-config/slack-config-1.png?classes=border,shadow)
<p align="center">Create new app on this [page](https://api.slack.com/apps?new_app=1)</p>

![slack-2](screenshots/slack-config/slack-config-2.png?classes=border,shadow)
<p align="center">Add app as a Bot</p>

![slack-3](screenshots/slack-config/slack-config-3.png?classes=border,shadow)
<p align="center">Setup a name or image of your Bot</p>

![slack-4](screenshots/slack-config/slack-config-4.png?classes=border,shadow)
![slack-5](screenshots/slack-config/slack-config-5.png?classes=border,shadow)
<p align="center">Install app to your workspace</p>


![slack-6](screenshots/slack-config/slack-config-6.png?classes=border,shadow)
<p align="center">Copy Oauth Access Token</p>


## Setup Slack notification in Osmedeus

This is optional config, you don't have to do this to get the tools done.

{{% notice tip %}}
You can only provide **REPORT_CHANNEL** and **SLACK_BOT_TOKEN** to get less verbose notification.
{{% /notice %}}


**STATUS_CHANNEL** is the place to put notifications.

**REPORT_CHANNEL** is the place to put output file.

**LOG_CHANNEL** is the place to put command was executed.

**STDS_CHANNEL** is the place to put all stdout.

**SLACK_BOT_TOKEN** is bot API or user API token that have permission to access channel above.

```
export LOG_CHANNEL=CGXXXXXX
export STATUS_CHANNEL=CGXXXXXX
export REPORT_CHANNEL=CGXXXXXX
export STDS_CHANNEL=CGXXXXXXX
export SLACK_BOT_TOKEN=xoxb-11
```

## Other token

```
export GITHUB_API_KEY=xxx
```

## Update token to db

Add those line above to your `~/.bashrc` or `~/.zshrc` or whatever of yours and `source ~/.bashrc` then run

```
python3 scripts/reload.py
```

Osmedeus auto pickup these environment variables and add to config file  `server.conf` file