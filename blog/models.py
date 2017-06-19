from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean
from blog.database import Base

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(50))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.name

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True)
    description = Column(Text)
    author = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=None)

    def __init__(self, title, description, author, created_at):
        self.title = title
        self.description = description
        self.author = author
        self.created_at = created_at

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    time = Column(DateTime)
    article = Column(Integer, ForeignKey('articles.id'))
    user = Column(Integer, ForeignKey('users.id'))

    def __init__(self, text, time, article, user):
        self.text = text
        self.time = time
        self.article = article
        self.user = user
