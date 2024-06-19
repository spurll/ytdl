from flask_wtf import FlaskForm
from wtforms import StringField, RadioField
from wtforms.validators import DataRequired


class DownloadForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired()])
    fmt = RadioField(
        'Format',
        choices=[
            ('m4a', 'Audio (M4A)'),
            ('mp4', 'Video (MP4)')
        ],
        default='mp4'
    )

