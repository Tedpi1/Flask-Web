from .models import User
from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
auth=Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return render_template('login.html')
@auth.route('/logout')
def logout():
    return render_template('home.html')
@auth.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        email=request.form.get('email')
        username=request.form.get('username')
        password=request.form.get('password')
        password1=request.form.get('password1')
        if len(email)<4:
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
            flash('Account created', category='success')
            return redirect(url_for('views.home'))
    return render_template('signup.html')