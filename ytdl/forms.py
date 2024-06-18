from flask_wtf import FlaskForm
from wtforms import StringField, RadioField
from wtforms.validators import DataRequired


class DownloadForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired()])
    fmt = RadioField(
        'Format',
        choices=[
            ('mp3', 'Audio (MP3)'),
            ('wav', 'Audio (WAV)'),
            ('v', 'Video')
        ],
        default='mp3'
    )

