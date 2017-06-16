from flask import Flask
from flask.ext.login import LoginManager
from flask_sqlalchemy import SQLAlchemy

blog = Flask(__name__)
blog.config.from_object('config')

login = LoginManager()
login.init_app(blog)
login.login_view = 'login'

db = SQLAlchemy(blog)
from blog import views, models, forms