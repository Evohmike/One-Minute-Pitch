
# from flask import render_template,request,redirect,url_for,abort
# from flask_login import login_user,login_required,current_user,logout_user
# from ..models import User
# from .forms import LoginForm,RegistrationForm
# from . import auth

# # Views
# @auth.route('/login', methods=["GET","POST"])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('main.dashboard'))
#     title = 'Login'
#     Form = LoginForm()
#     Error=False
#     if Form.validate_on_submit():
#         username=str(Form.username.data)
#         password=str(Form.password.data)
#         if username and password:
#             user=User.query.filter(User.username==username).first()
#             if user and user.verifypass(password):
#                 print(password)
#                 login_user(user,Form.remember.data)
#                 return redirect(url_for('main.dashboard'))
#             Error='Wrong Username or Password'
#         else:
#             Error='Please Type a Username or Password'
#     return render_template('login.html', title = title ,Form=Form,Error=Error)

# @auth.route('/register', methods=["GET","POST"])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('main.dashboard'))
#     title = 'Register'
#     Form = RegisterForm()
#     Error=False
#     if Form.validate_on_submit():
#         username=str(Form.username.data)
#         password=str(Form.password.data)
#         if username and password:
#             user=User.query.filter(User.username==username).first()
#             if not user:
#                 user=User(username=username,passwd=password)
#                 user.save()
#                 return redirect(url_for('auth.login'))
#             Error='Username Already taken'
#     return render_template('register.html', title = title ,Form=Form,Error=Error)

# @auth.route('/logout')
# def logout():
#     if current_user.is_authenticated:
#         logout_user()
#     return redirect(url_for('main.dashboard'))





from flask import render_template, redirect, url_for, request, flash
from . import auth
from flask_login import login_required, login_user, logout_user
from ..models import User
from .forms import LoginForm, RegistrationForm
from .. import db


@auth.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "login"
    return render_template('auth/login.html', login_form=login_form, title=title)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = 'New Account'
    return render_template('auth/register.html', registration_form=form)


