from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators
from blog.models import Article

class UpdateArticle(FlaskForm):
    title = StringField('Title', [
        validators.Length(min=1),
        validators.DataRequired(message='This field must not be empty')
    ])
    description = TextAreaField('Description', [
        validators.Length(min=1),
        validators.DataRequired(message='This field must not be empty')
    ])
