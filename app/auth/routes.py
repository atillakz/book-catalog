from flask import render_template,request, flash, redirect,url_for
from app.auth.forms import RegistrationForm
from app.auth import auth as at
from app.auth.models import User
from app.auth.forms import LoginForm
from flask_login import login_user, logout_user,login_required,current_user

@at.route('/register', methods = ['GET', 'POST'])

def register():

    if current_user.is_authenticated:
        flash("you already signed in")

        return redirect(url_for('main.display'))

    form = RegistrationForm()

    if form.validate_on_submit():

        User.create_user(

            user = form.name.data,

            email= form.email.data,

            password = form.password.data
        )

        flash('Registration Succesful')

        return redirect(url_for('auth.do_the_login'))


    return render_template('registration.html', form = form)

@at.route('/login', methods = ['GET', 'POST'])

def do_the_login():

    if current_user.is_authenticated:
        flash("you already signed in")

        return redirect(url_for('main.display'))


    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(user_email = form.email.data).first()
        if not user or not user.check_password(form.password.data):
            flash('Invalid Credentials')
            return redirect(url_for('auth.do_the_login'))

        login_user(user, form.stay_logged_in.data)

        return redirect(url_for('main.display'))



    return render_template('login.html', form = form)

@at.route('/logout')
@login_required
def log_out():
    logout_user()
    return redirect(url_for('main.display'))


@at.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
