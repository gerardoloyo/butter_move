from api import db

class State(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    abbreviation = db.Column(db.String(2), unique=True, nullable=False)
    normal_commission = db.Column(db.Float, nullable=False)
    premium_commission = db.Column(db.Float, nullable=False)
    iva = db.Column(db.float, nullable=False)
    base_discount = db.Column(db.float, nullable=False)
    total_discount = db.Column(db.float, nullable=False)
    premium_discount = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return f"State('{self.abbreviation}', {self.normal_commission}, {self.premium_commission})"
