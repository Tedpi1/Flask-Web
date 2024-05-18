from flask import Blueprint, render_template, request, flash
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
        phone=request.form.get('phone')
        username=request.form.get('username')
        password1=request.form.get('password')
        password2=request.form.get('password1')
        if len(email)<4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(username)<3:
            flash('Username must be greater than 2 characters', category='error')
        elif len(phone<10):
            flash('Phone number must be greater than 10 characters', category='error')
        elif len(password1)<7:
            flash('Password must be greater than 7 characters', category='error')
        elif password1!=password2:
            flash('Passwords do not match', category='error')
        else:
            flash('Account created', category='success')
            return render_template('home.html')
        
    return render_template('signup.html')