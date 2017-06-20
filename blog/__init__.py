from flask import Flask
from flask_login import LoginManager
from .models import Users

blog = Flask(__name__)
blog.config.from_object('config')

log = LoginManager()
log.init_app(blog)
log.login_view = '/login'

from blog.database import db_session, init_db

from blog import forms, views
init_db()

@blog.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@log.user_loader
def load_user(user_id):
    return Users.query.filter(Users.name == user_id).first()


