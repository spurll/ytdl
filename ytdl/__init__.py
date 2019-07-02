from flask import Flask
import os


app = Flask(__name__)
app.config.from_object('config')


if not os.path.exists(app.config['VIDEO_DIR']):
    os.makedirs(app.config['VIDEO_DIR'])


from ytdl import views
