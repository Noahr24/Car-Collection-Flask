from flask import Blueprint, render_template, request
from car_inventory.forms import UserLoginForm

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserLoginForm
    if request.method == "POST":
        email = form.email.data
        password = form.password.data
    return render_template('signup.html', form = form)

@auth.route('/signin')
def signin():
    return render_template('signin.html')