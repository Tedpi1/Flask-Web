from .models import User
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user #current user uses usermixin 
auth=Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('Email does not exist', category='error')
    return render_template('login.html', user= current_user)
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
@auth.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        email=request.form.get('email')
        username=request.form.get('username')
        password=request.form.get('password')
        password1=request.form.get('password1')
        user=User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')
        elif len(email)<4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(username)<3:
            flash('Username must be greater than 2 characters', category='error')
        elif len(password)<7:
            flash('Password must be greater than 7 characters', category='error')
        elif password!=password1:
            flash('Passwords do not match', category='error')
        else:
            new_user=User(email=email, username=username, password=generate_password_hash(password, method='scrypt'))
            #adding account to the databases
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created', category='success')
            return redirect(url_for('views.home'))
    return render_template('signup.html', user=current_user)