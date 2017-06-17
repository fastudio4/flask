from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators


class LoginForm(FlaskForm):
    pass

class RegistrUser(FlaskForm):
    username = StringField('Username', [validators.Length(min=1, max=50)])
    email = StringField('Email', [validators.Email()])
    password = PasswordField('Password', [validators.Length(min=1)])