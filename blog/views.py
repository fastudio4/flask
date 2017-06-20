from datetime import datetime
from flask import render_template, redirect, flash, session, url_for, request, g, logging
from flask_login import login_user, logout_user, current_user, login_required
from blog.forms import *
from .models import Users, Article
from . import blog, log, db_session


@blog.route('/')
@blog.route('/index')
def home():
    return render_template('index.html')

@blog.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterUser(request.form)
    if request.method == 'POST' and form.validate():
        user = Users(form.username.data, form.email.data, form.password.data)
        db_session.add(user)
        db_session.commit()
        login_user(user)
        flash('You registered, please enter site')
        return redirect('/')
    return render_template('register.html', form=form, title='Register form')


@blog.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginUser(request.form)
    if request.method == 'POST' and form.validate():
        user = Users.query.filter_by(name=form.name.data).first()
        login_user(user, remember=form.remember.data)
        flash('You login in site')
        return redirect('/')
    return render_template('login.html', form=form, title='Login form')

@blog.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

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

@blog.route('/logout')
@login_required
def update_article():
    pass

@blog.route('/logout')
@login_required
def delete_article():
    pass
