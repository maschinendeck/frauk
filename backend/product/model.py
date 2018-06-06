import datetime
from backend import db, Base

class Product(Base):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True)
    price = db.Column(db.Integer, default=0)
    bottle_size_l = db.Column(db.Float)
    caffeine_mg = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())
    active = db.Column(db.Boolean, default=True)
