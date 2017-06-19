from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean
from blog.database import Base

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(50))
    is_authenticated = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    is_anonymous = Column(Boolean, default=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def get_id(self):
        return str(self.id)

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True)
    description = Column(Text)
    author = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=None)
    like = Column(Integer, default=0)

    def __init__(self, title, description, author, create):
        self.title = title
        self.description = description
        self.author = author
        self.create = create

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
