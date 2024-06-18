from . import td
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(td.Model):
    id = td.Column(td.Integer, primary_key=True)
    data = td.Column(td.String(10000))
    date = td.Column(td.DateTime(timezone=True), default=func.now())
    user_id = td.Column(td.Integer, td.ForeignKey('user.id'))


class User(td.Model, UserMixin):
    id = td.Column(td.Integer, primary_key=True)
    email = td.Column(td.String(150), unique=True)
    password = td.Column(td.String(150))
    username= td.Column(td.String(150))
    notes = td.relationship('Note')