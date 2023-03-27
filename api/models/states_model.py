from api import db

class State(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    abbreviation = db.Column(db.String(2), unique=True, nullable=False)
    normal_commission = db.Column(db.Float, nullable=False)
    premium_commission = db.Column(db.Float, nullable=False)
    iva = db.Column(db.Float, nullable=False)
    base_discount = db.Column(db.JSON, nullable=False)
    total_discount = db.Column(db.JSON, nullable=False)
    premium_discount = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return f"State(id={self.id}, abbreviation='{self.abbreviation}', normal_commission={self.normal_commission}, premium_commission={self.premium_commission}, iva={self.iva}, base_discount={self.base_discount}, total_discount={self.total_discount}, premium_discount={self.premium_discount})"

