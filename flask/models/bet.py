from . import db

class Bet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_a_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    pizza_count_owed = db.Column(db.Integer, nullable=False)
    # payments = db.relationship('Payment', backref='bet')
    

    def __init__(self):
        self.is_settled = False


