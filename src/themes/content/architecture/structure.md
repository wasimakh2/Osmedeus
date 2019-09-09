---
title: "Structure"
date: 2019-09-09T00:25:58+07:00
draft: false
weight: 1
---

## Osmedeus Structure

``` bash
.
├── lib  # contain lib to for Server and client
│   ├── alias
│   ├── client
│   ├── core
│   ├── mode
│   ├── noti
│   ├── reporter
│   ├── sender  # API call from client to REST API server
│   └── workflow  # predefine command here
├── modules  # Logic for each module
├── scripts
└── server  # Django API Server
    ├── api
    ├── rest
    └── ui
```


## Result Structure

By default your output will be store in `~/.osmedeus/workspaces/`. Each folder store seprated output for each routine,

```bash
your_target
├── fingerprint # technoly found
│   └── responses
├── ipspace # All IP found
├── links
│   └── raw
├── portscan
│   └── screenshot
│       └── raw-gowitness
├── probing  # store subdomain can be reachable
├── screenshot
│   ├── your_target-aquatone
│   │   ├── headers
│   │   ├── html
│   │   └── screenshots
│   └── raw-gowitness
├── stoscan 
└── subdomain  # All subdomain found
    └── amass-your_target

```
