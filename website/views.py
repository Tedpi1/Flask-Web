from flask import Blueprint, render_template
from flask_login import login_required, current_user #current user uses usermixin 
#defining blueprint
views=Blueprint('views',__name__)
#defining a view
@views.route('/')
@login_required
def home():
    return render_template("home.html", user= current_user) 