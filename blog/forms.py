from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, validators


class LoginForm(Form):
    pass

class RegistrUser(Form):
    username = StringField('Username', [validators.Length(min=1, max=50)])
    email = StringField('Email', [validators.Email()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Password incorrect')
    ])
