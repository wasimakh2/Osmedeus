---
title: "Report Mode"
date: 2019-08-08T21:47:55+07:00
draft: true
---

## Report mode

### Usage

```
[Report Mode]
===================
sum         - Summary report
list        - List avalible workspace
short       - Only print final output of each module
full        - Print all output of each module
path        - Only print final path of each module
raw         - Print all stdout of each module
html        - Export to html

[Filter module]
===================
subdomain, recon, assetfinding
takeover, screenshot
portscan, dirbrute, vulnscan
gitscan, cors, ipspace, sslscan, headers


[Report Usage]
===================
./osemdeus.py --report <mode> -t <workspace> [-m <module>]

[Example Commands]
===================
./osemdeus.py -t example.com --report list
./osemdeus.py -t example.com --report sum
./osemdeus.py -t example.com --report path
./osemdeus.py -t example.com --report short
./osemdeus.py -t example.com -m subdomain --report short
./osemdeus.py -t example.com -m subdomain, portscan --report short
./osemdeus.py -t example.com -m subdomain, portscan --report full

```


### Examples

` ./osmedeus.py --report sum -t example.com `

![Reports](https://raw.githubusercontent.com/j3ssie/Osmedeus/master/imgs/osmedeus-report.png?classes=border,shadow)

***
