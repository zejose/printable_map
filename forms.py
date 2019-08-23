from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField


class NavigationForm(FlaskForm):

    search = StringField('Search')

    zoom = IntegerField('Zoom')

    map_style = SelectField(
        'Theme',
        choices=[
            ('OpenStreetMap', 'OpenStreetMap'),
            ('stamenterrain', 'stamenterrain')
        ]
    )

    submit = SubmitField('Refresh')
