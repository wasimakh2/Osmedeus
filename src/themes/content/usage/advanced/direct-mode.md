---
title: "Direct Mode"
date: 2019-08-08T21:44:32+07:00
draft: false
---

### Usage of Direct Mode

The goal of this mode is to create lots of advanced alias for your routine.

```
./osmedeus.py -m <modules> -i/-I single_input/list_of_inputs.txt [-t result_folder]  
```

{{% notice tip %}}
you can even use multiple modules by seperate it with `,`.
{{% /notice %}}

 E.g: ```./osmedeus.py -m "portscan,vuln" -I list_of_targets.txt -t output_folder```

#### Modules supported direct mode

```
List module
===========
subdomain   - Scanning subdomain and subdomain takerover
portscan    - Screenshot and Scanning service for list of domain
screenshot  - Screenshot list of hosts
asset       - Asset finding like URL, Wayback machine
vuln        - Scanning version of services and checking vulnerable service
git         - Scanning for git repo
dirb        - Do directory search on the target
```

***

#### Subdomain
This module not required input options (-i/-I).
```
./osmedeus.py -m subdomain -t example.com
./osmedeus.py -m subdomain -t example.com --slow 'subdomain'
```

#### Portscan and VulnScan

```
./osmedeus.py -m portscan -i "1.2.3.4/24"
./osmedeus.py -m portscan -I list_of_targets.txt
./osmedeus.py -m "portscan,vuln" -I list_of_targets.txt -t output_folder
```

#### AssetFinding and Screenshot

```
./osmedeus.py -m asset -i "github.com" -t "result_folder"
./osmedeus.py -m "asset,screen" -I list_of_targets.txt
```

#### GitScan and DirbScan
```
./osmedeus.py -m git -i https://github.com/do_not/try_my_repo -t sample1
./osmedeus.py -m dirb -I /tmp/list_of_hosts.txt -t sample2

```



