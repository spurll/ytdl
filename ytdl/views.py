import os.path
from tempfile import mkdtemp
from subprocess import run
from flask import render_template, flash, request, send_from_directory

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

    fmt = form.fmt.data

    command = [
        'youtube-dl', form.url.data, '-o',
        os.path.join(directory, '%(title)s.%(ext)s')
    ]

    if fmt != 'v':
        command.extend(['-x', f'--audio-format={fmt}'])

    try:
        # Download the file
        process = run(command, check=True)

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

