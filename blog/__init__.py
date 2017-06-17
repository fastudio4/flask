from flask import Flask
from flask_login import LoginManager


blog = Flask(__name__)
blog.config.from_object('config')

login = LoginManager()
login.init_app(blog)
login.login_view = 'login'

from blog.database import db_session, init_db
from blog import forms, views
init_db()
@blog.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


