from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from blog.models import Users

class LoginUser(FlaskForm):
    name = StringField('Username', [validators.Length(min=1, max=50), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=6), validators.DataRequired()])

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        user_ex = Users.query.filter_by(name=self.name.data).first()
        if user_ex is None:
            self.name.errors.append('Incorrect user')
            return False
        elif self.password.data != user_ex.password:
            self.password.errors.append('Incorrect password')
            return False
        return True

