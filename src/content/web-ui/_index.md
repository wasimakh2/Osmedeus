---
title: "Web UI"
date: 2019-08-08T21:13:31+07:00
draft: true
weight: 5
---

{{% notice note %}}
Note that we're using self-signed certificate so make sure you trust that and access via **HTTPS**.
{{% /notice %}}

![CA Warning](https://user-images.githubusercontent.com/23289085/62714231-5a6c0e80-ba28-11e9-9f9b-d2b202808cb8.png?classes=border,shadow)

![Login](https://user-images.githubusercontent.com/23289085/62714564-06adf500-ba29-11e9-989d-1bc62b210bde.png?classes=border,shadow)


#### Local
If you're run Osmedeus on the local machine just access https://127.0.0.1:5000 and fill the credentials from your `config.conf` file. (by default, it's on `~/.osmedeus/config.conf`)

****
#### Remote
If you're run Osmedeus server and client separately, you gonna need to change **Remote URL** in the login sections on the Web UI.

![Web UI](https://user-images.githubusercontent.com/23289085/62714373-a1f29a80-ba28-11e9-8acc-afbb47bed6bf.png?classes=border,shadow)


Check out this wiki for more [details](/architecture/) about running remote Osmedeus.

### Credits
* React components is powered by [Carbon](https://www.carbondesignsystem.com/) and [carbon-tutorial](https://github.com/carbon-design-system/carbon-tutorial).

* Awesomes artworks are powered by [Freepik](http://freepik.com) at [flaticon.com](http://flaticon.com).