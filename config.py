import os

DEBUG = True
PORT = '5000'
CSRF_ENABLE = True
SECRET_KEY = 'Idontno'

BASEDIR = os.path.abspath(os.path.dirname(__file__))

DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'blog.db')
# SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'db_repository')