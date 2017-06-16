from flask import render_template, redirect, flash, session, url_for, request, g, logging
# from flask.ext.login import login_user, logout_user, current_user, login_required
from .forms import RegistrUser
from .models import Users
from blog import blog, db, login

@blog.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrUser(request.form)
    if request.method == 'POST' and form.validate():
        user = Users(form.username.data, form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You registered, please enter site')
    else:
        return render_template('register.html', form=form)