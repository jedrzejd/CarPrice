from wtforms import StringField, SubmitField, validators, Form


class TextForm(Form):
    link = StringField('Link', [validators.Length(min=4, max=200), validators.DataRequired()])
    submit = SubmitField('Wylicz')