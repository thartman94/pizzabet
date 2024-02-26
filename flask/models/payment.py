from . import db

class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)
    pizza_count_paid = db.Column(db.Integer, nullable=False)
    bet_id = db.Column(db.Integer, db.ForeignKey('bet.id'), nullable=False)
    accepted = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, pizza_count_paid, bet_id, accepted=False):
      self.pizza_count_paid = pizza_count_paid
      self.bet_id = bet_id
      self.accepted = accepted
        
    def json(self):
      return {
        "pizza_count_paid" : self.pizza_count_paid,
        "bet_id" : self.bet_id,
        "accepted" : self.accepted
      }


