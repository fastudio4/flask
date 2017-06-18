from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from blog.models import Users

class RegisterUser(FlaskForm):
    username = StringField('Username', [validators.Length(min=1, max=50), validators.DataRequired()])
    email = StringField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [
        validators.Length(min=6),
        validators.DataRequired()])

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False
        user_ex = Users.query.filter_by(email=self.email.data).first()
        if user_ex is not None:
            self.email.errors.append('Email is already in use')
            return False
        return True