from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class UpdateArticle(FlaskForm):
    title = StringField('Title', [validators.DataRequired()])
    description = TextAreaField('Description', [validators.DataRequired()])

    def validate(self):
        vr = FlaskForm.validate(self)
        if vr is None:
            return False
        if self.title == '':
            self.title.errors.append('This field must not be empty')
            return False
        if self.description == '':
            self.description.errors.append('This field must not be empty')
            return False
        return True
