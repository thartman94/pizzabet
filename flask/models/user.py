

from . import db
from flask import jsonify


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    bets = db.relationship('Bet', backref='person', lazy=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def json(self):
      return {
        "username": self.username,
        "email": self.email
      }

