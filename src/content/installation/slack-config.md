---
title: "Slack Config"
date: 2019-08-08T21:51:02+07:00
draft: true
weight: 3
---

This is optional config you don't have to do this to get the tools done.

{{% notice tip %}}
You can only provide **REPORT_CHANNEL** and **SLACK_BOT_TOKEN** to get less verbose noti.
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

Add those line above to your `~/.bashrc` or `~/.zshrc` or whatever of yours and Osmedeus auto pickup these environment variables and add to config file or you have to edit manually in your `config.conf` file