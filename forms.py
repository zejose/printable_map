from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class NavigationForm(FlaskForm):

    search = StringField('Search')

    zoom = IntegerField('Zoom')

    map_style = SelectField(
        'Theme',
        choices=[
            ('OpenStreetMap', 'OpenStreetMap'),
            ('stamenterrain', 'stamenterrain'),
            ('stamentoner', 'stamentoner'),
            ('CartoDB positron', 'CartoDB positron'),
            ('CartoDB dark_matter', 'CartoDB dark_matter')
        ]
    )

    submit = SubmitField('Refresh')
