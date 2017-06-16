from blog import db

class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True)
    user_email = db.Column(db.String(50), unique=True)
    user_password = db.Column(db.String(50))

    def __init__(self, user_name, user_email, user_password):
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password

class Article(db.Model):
    __tablename__ = 'articles'
    article_id = db.Column(db.Integer, primary_key=True)
    article_title = db.Column(db.String(100), unique=True)
    article_description = db.Column(db.Text)
    article_author = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    article_create = db.Column(db.DateTime, default=None)
    article_like = db.Column(db.Integer, default=0)

    def __init__(self, article_title, article_description, article_author, article_create):
        self.article_title = article_title
        self.article_description = article_description
        self.article_author = article_author
        self.article_create = article_create

class Comments(db.Model):
    __tablename__ = 'comments'
    comment_id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.Text)
    comment_time = db.Column(db.DateTime)
    comment_article = db.Column(db.Integer, db.ForeignKey('articles.article_id'))
    comment_user = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __init__(self, comment_text, comment_time, comment_article, comment_user):
        self.comment_text = comment_text
        self.comment_time = comment_time
        self.comment_article = comment_article
        self.comment_user = comment_user
