from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    notes=db.relationship('Note')
class Note(db.Model):
    id=db.column(db.Integer, primary_key=True)
    data=db.column(db.String(1000))
    date=db.Column(db.DateTime(timezone=True) default=func.now())
    use_id=db.column(db.Integer, db.ForeignKey('user.id'))