from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators

class CommentsArticle(FlaskForm):
    comments = TextAreaField('Comments', [validators.Length(min=1), validators.DataRequired()])
