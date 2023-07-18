from Flaskmarket import app
from Flaskmarket import db

class Items(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(length=30), nullable = False, unique=True)
    barcode = db.Column(db.String(length=12), nullable = False, unique=True)
    price = db.Column(db.Integer(),nullable=False)
    desc = db.Column(db.String(length=12), nullable = False, unique=True)

with app.app_context():
    db.create_all()