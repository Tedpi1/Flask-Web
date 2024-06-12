from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True,)
    email = db.Column(db.String(120), unique=True,)
    password = db.Column(db.String(120))
    notes=db.relationship('notes')
    
class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data=db.column(db.String(1000),)
    date=db.column(db.DateTime(timezone=True), default=func.now())
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))