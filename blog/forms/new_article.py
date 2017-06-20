from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class NewArticle(FlaskForm):
    title = StringField('Title article', [validators.Length(min=1, max=100), validators.DataRequired()])
    description = TextAreaField('Description', [validators.DataRequired()])



