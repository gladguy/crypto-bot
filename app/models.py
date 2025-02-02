from app import db

class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pair_address = db.Column(db.String(42), unique=True)
    chain_id = db.Column(db.String(10))
    created_at = db.Column(db.DateTime)

class PriceHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pair_address = db.Column(db.String(42))
    timestamp = db.Column(db.DateTime)
    price = db.Column(db.Float)