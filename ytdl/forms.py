from flask_wtf import FlaskForm
from wtforms import TextField, RadioField
from wtforms.validators import Required


class DownloadForm(FlaskForm):
    url = TextField('URL', validators=[Required()])
    fmt = RadioField(
        'Format',
        choices=[
            ('mp3', 'Audio (MP3)'),
            ('wav', 'Audio (WAV)'),
            ('v', 'Video')
        ],
        default='mp3'
    )

