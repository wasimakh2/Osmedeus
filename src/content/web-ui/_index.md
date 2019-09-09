---
title: "Web UI"
date: 2019-08-08T21:13:31+07:00
draft: false
weight: 5
---


#### Local

![Screen Shot 2019-09-08 at 23 58 54](https://user-images.githubusercontent.com/23289085/64491739-eecec880-d295-11e9-848d-c3e944d98781.png)


If you're run Osmedeus on the local machine just access http://127.0.0.1:8000, fill the credentials from your `client.conf` file. (by default, it's on `~/.osmedeus/client.conf`)

You can also create a new one via [Django authentication system](https://docs.djangoproject.com/en/2.2/topics/auth/default/).

```
python3 server/manage.py createsuperuser
```

****

#### Remote

If you're run Osmedeus server and client separately, you gonna need to change **Remote URL** in the login sections on the Web UI.

![Web UI](https://user-images.githubusercontent.com/23289085/62714373-a1f29a80-ba28-11e9-8acc-afbb47bed6bf.png?classes=border,shadow)


Check out this wiki for more [details](/architecture/) about running remote Osmedeus.

### Credits
* React components is powered by [Carbon](https://www.carbondesignsystem.com/) and [carbon-tutorial](https://github.com/carbon-design-system/carbon-tutorial).

* Awesomes artworks are powered by [Freepik](http://freepik.com) at [flaticon.com](http://flaticon.com).