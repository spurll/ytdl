import os, time, sys, shutil
from tempfile import mkdtemp
from subprocess import run
from flask import render_template, flash, request, send_from_directory
from yt_dlp import YoutubeDL

from ytdl import app
from ytdl.forms import DownloadForm


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Download.
    """
    form = DownloadForm()

    if request.method == 'GET':
        return render_template('index.html', form=form)

    if not form.validate_on_submit():
        flash('Invalid form data. Please try again.')
        return render_template('index.html', form=form)

    # Create temporary directory
    directory = mkdtemp(dir=app.config['VIDEO_DIR'])

    print(form.fmt.data)

    options = {
        'outtmpl': os.path.join(directory, '%(title)s.%(ext)s'),
        'format': form.fmt.data,
        'cachedir': False
    }

    try:
        with YoutubeDL(options) as ytdl:
            ytdl.download(form.url.data)
    except Exception as e:
        print(e)
        flash('Error: Could not download/convert the video as requested.')
        return render_template('index.html', form=form)

    files = os.listdir(directory)
    if not files:
        flash('Error: Could not find the file specified.')
        return render_template('index.html', form=form)

    # Send the file to the user
    return send_from_directory(directory, files[0], as_attachment=True)


def clean():
    """
    Clear downloads that are more than a week old.
    """
    now = time.time()

    for file in os.listdir(app.config['VIDEO_DIR']):
        path = os.path.join(app.config['VIDEO_DIR'], file)

        # If it hasn't been modified in the last week, remove it
        if os.stat(path).st_mtime < now - 7 * 86400:
            try:
                print(f'Removing {path}...')
                if os.path.isfile(path) or os.path.islink(path):
                    os.unlink(path)
                elif os.path.isdir(path):
                    shutil.rmtree(path)

            except Exception as e:
                print(f'Failed to delete {path}: {e}')
