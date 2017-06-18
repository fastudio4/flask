from flask import render_template, redirect, flash, session, url_for, request, g, logging

from flask.ext.login import login_user, logout_user, current_user, login_required
from blog.forms import *
from .models import Users
from . import blog, login, db_session


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
        flash('You registered, please enter site')
        return redirect('/')
    return render_template('register.html', form=form, title='Register form')

@blog.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginUser(request.form)
    if request.method == 'POST' and form.validate():
        login_user(form.name.data)
        flash('You login in site')
        return redirect('/')
    return render_template('login.html', form=form, title='Login form')