---
title: "Docker Setup"
date: 2019-08-08T21:30:23+07:00
draft: false
weight: 1
---


## Using Docker

Check out [docker-osmedeus](https://github.com/mablanco/docker-osmedeus) by [mabnavarrete](https://twitter.com/mabnavarrete) for docker installation.

### TL;DR
Run this command to pull container and install Osmedeus.
#### Installation
```
docker run -d --net host --name osmedeus mablanco/osmedeus
```

#### Simple usage
```
docker exec -it osmedeus ./osmedeus.py --client -t example.com
```

or access container through bash then navigate to `~/` and you're good to go.

```
docker exec -it osmedeus /bin/bash -i
```

#### Access the UI
Credentials by default will place in `~/.osmedeus/config.conf`. 
Make sure to change the Remote api in Configuration tab to your interface that you're running docker.
