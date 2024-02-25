from . import db

class Bet(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)
    pizza_count_paid = db.Column(db.Integer, nullable=False)
    # bet_id = db.Column(db.Integer, db.ForeignKey('bet.id'))
    

    def __init__(self, user_a: int, user_b: int, witnesses: list[int]):
        self.user_a = user_a
        self.user_b = user_b
        self.witnesses = witnesses
        self.is_settled = False


