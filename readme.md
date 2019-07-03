ytdl
====

A web application for downloading audio/video from YouTube. Basically just a web wrapper
for [youtube-dl](https://ytdl-org.github.io/youtube-dl/) with a stripped-down feature set.

Usage
=====

Installation
------------

You'll need to install [youtube-dl](https://ytdl-org.github.io/youtube-dl/). It's
recomended that you keep it updated (e.g., via a cron job).

```
youtube-dl -U
```

You'll also need to install ffmpeg/avconv.

Requirements
------------

* flask
* flask-wtf
* [youtube-dl](https://ytdl-org.github.io/youtube-dl/)
* ffmpeg

Starting the Server
-------------------

Start the server with `run.py`. By default it will be accessible at `localhost:9999`. To
make the server world-accessible or for other options, see `run.py -h`.

If you're having trouble configuring your sever, I wrote a
[blog post](http://blog.spurll.com/2015/02/configuring-flask-uwsgi-and-nginx.html)
explaining how you can get Flask, uWSGI, and Nginx working together.

Bugs and Feature Requests
=========================

Feature Requests
----------------

* Add an animated "converting" image (with "this may take a few minutes")
* Delete downloads after a while
* Include recommended cron lines for deleting old downloads and updating ytdl

Known Bugs
----------

None

Thanks
======

Thanks to the team behind [youtube-dl](https://ytdl-org.github.io/youtube-dl/)!

License Information
===================

Written by Gem Newman. [Website](http://spurll.com) | [GitHub](https://github.com/spurll/) | [Twitter](https://twitter.com/spurll)

This work is licensed under Creative Commons [BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/).

JQuery included under the [MIT "Expat" License](https://opensource.org/licenses/MIT).

Remember: [GitHub is not my CV](https://blog.jcoglan.com/2013/11/15/why-github-is-not-your-cv/).

