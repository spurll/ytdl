from os import urandom, path


# Web Server
CSRF_ENABLED = True
SECRET_KEY = urandom(30)
PROPAGATE_EXCEPTIONS = True

basedir = path.abspath(path.dirname(__file__))
VIDEO_DIR = path.join(basedir, 'download')
