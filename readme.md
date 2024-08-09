ytdl
====

A web application for downloading audio/video from YouTube. Basically just a web wrapper
for [yt-dlp](https://pypi.org/project/yt-dlp) with a stripped-down feature set.

Usage
=====

Installation
------------

You'll need to install [yt-dlp](https://pypi.org/project/yt-dlp/). It's recomended that
you keep it updated (e.g., via a cron job):

```sh
python3 -m pip install --upgrade yt-dlp
```

You'll also need to install ffmpeg.

Requirements
------------

* flask (3.0+)
* flask-wtf
* yt-dlp
* ffmpeg

Starting the Server
-------------------

Start the server with `run.py`. By default it will be accessible at `localhost:9999`. To
make the server world-accessible or for other options, see `run.py -h`.

If you're having trouble configuring your sever, I wrote a
[blog post](http://blog.spurll.com/2015/02/configuring-flask-uwsgi-and-nginx.html)
explaining how you can get Flask, uWSGI, and Nginx working together.

Cron Jobs
---------

To keep `yt-dlp` up to date:

```cron
15 5 * * * source /opt/ytdl/venv/bin/activate && pip install --upgrade yt-dlp > /dev/null ; deactivate
```

To periodically delete the contents of the `downloads` folder (where downloaded videos are
stored temporarily to be served to users):

```cron
40 3 * * 0 python3 -c "from os import chdir; chdir('/opt/ytdl/'); import ytdl; ytdl.views.clean()" > /dev/null 
```

Bugs and Feature Requests
=========================

Feature Requests
----------------

* Add an animated "converting" image (with "this may take a few minutes")

Known Bugs
----------

None

Thanks
======

Thanks to the team behind [yt-dlp](https://ytdl-org.github.io/youtube-dl/)!

License Information
===================

Written by Gem Newman. [Website](http://spurll.com) | [GitHub](https://github.com/spurll/) | [Twitter](https://twitter.com/spurll)

This work is licensed under Creative Commons [BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/).

JQuery included under the [MIT "Expat" License](https://opensource.org/licenses/MIT).

Remember: [GitHub is not my CV](https://blog.jcoglan.com/2013/11/15/why-github-is-not-your-cv/).

