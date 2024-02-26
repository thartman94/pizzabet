from sqlalchemy.dialects.postgresql import ARRAY
from datetime import date

from . import db

class Bet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    settled_date = db.Column(db.DateTime, nullable=True)
    
    user_a_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_b_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    winner = db.Column(db.Integer, db.ForeignKey('users.id'))
    witness_ids = db.Column(ARRAY(db.Integer, db.ForeignKey('users.id')))
    pizzas_owed_count = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.DateTime)
    
    payments = db.relationship('Payment', backref='bet')
    

    def __init__(self, user_a_id, user_b_id, witness_ids, pizzas_owed_count, start_date=date.today(), winner=None):
      self.settled_date = None
      self.winner = winner
      self.start_date = start_date
      self.pizzas_owed_count = pizzas_owed_count
      self.witness_ids = witness_ids
      self.user_b_id = user_b_id
      self.user_a_id = user_a_id
        
    def json(self):
      return {
        "start_date" : self.start_date,
        "settled_date" : self.settled_date,
        "pizzas_owed_count" : self.pizzas_owed_count,
        "winner" : self.winner,
        "witness_ids" : self.witness_ids,
        "user_a_id" : self.user_a_id,
        "user_b_id" : self.user_b_id
      }


