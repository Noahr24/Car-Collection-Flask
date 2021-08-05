from flask import Blueprint, render_template, request, redirect, flash
from flask.helpers import url_for
from car_inventory.forms import UserLoginForm
from car_inventory.models import User, db, check_password_hash
from flask_login import login_user

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserLoginForm()
    if request.method == "POST" and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print([email, password])

        user = User(email, password)
        db.session.add(user)
        db.session.commit()


        #Flashed messaged for successful sign up
        flash(f'You hsve successfully created user account {email}', 'user-created')
        #Redirecting to home page
        return redirect(url_for('site.home'))

    return render_template('signup.html', form = form)

@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(email, password)

        logged_user = User.query.filter(User.email == email).first()
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            flash('You were successfully loggin in.', 'auth-success')
            return redirect(url_for('site.home'))
        else:
            flash('Your Email/Passsword is incorrect', 'auth-failed')
            return redirect(url_for('auth.signin'))


    return render_template('signin.html', form = form)
