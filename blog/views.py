from datetime import datetime
from flask import render_template, redirect, flash, session, url_for, request, g, logging
from flask_login import login_user, logout_user, current_user, login_required
from blog.forms import *
from .models import Users, Article
from . import blog, db_session


@blog.route('/')
@blog.route('/index')
def home():
    articles = Article.query.all()
    return render_template('index.html', articles=articles)

@blog.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterUser(request.form)
    if request.method == 'POST' and form.validate():
        user = Users(form.username.data, form.email.data, form.password.data)
        db_session.add(user)
        db_session.commit()
        login_user(user)
        return redirect('/')
    return render_template('register.html', form=form, title='Register form')


@blog.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginUser(request.form)
    if request.method == 'POST' and form.validate():
        user = Users.query.filter_by(name=form.name.data).first()
        login_user(user, remember=form.remember.data)
        return redirect('/')
    return render_template('login.html', form=form, title='Login form')

@blog.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

@blog.route('/blog/<slug_title>')
def article(slug_title):
    article = Article.query.filter_by(slug=slug_title).first()
    return render_template('article.html', article=article, title=article.title)

@blog.route('/new', methods=['GET', 'POST'])
@login_required
def new_article():
    form = NewArticle(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        article = Article(form.title.data, form.description.data, current_user.name, datetime.utcnow())
        db_session.add(article)
        db_session.commit()
        return redirect('/index')
    return render_template('new.html', form=form, title='New article')

@blog.route('/update/<slug_title>', methods=['GET', 'POST'])
@login_required
def update_article(slug_title):
    article = Article.query.filter_by(slug=slug_title).first()
    form_out = UpdateArticle()
    form_out.title.data = article.title
    form_out.description.data = article.description
    if request.method == 'POST':
        form_in = UpdateArticle()
        if form_in.validate_on_submit():
            article.title = form_in.title.data
            article.description = form_in.description.data
            db_session.commit()
            return redirect('/blog/%s' % article.slug)
    return render_template('article_update.html', article=article, form=form_out, title='Update article')

@blog.route('/logout')
@login_required
def delete_article():
    pass
