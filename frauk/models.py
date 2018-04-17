import datetime
from frauk import db, Base
from sqlalchemy.orm import (relationship, backref)


class User(Base):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True)
    email = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())
    balance = db.Column(db.Integer, default=0)
    active = db.Column(db.Boolean, default=True)
    audit = db.Column(db.Boolean, default=True)

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

class Audit(Base):
    __tablename__ = 'audit'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    difference = db.Column(db.Integer, default=0)
    product_id = db.Column(db.ForeignKey('product.id'), nullable=False)
    product = relationship(
        Product,
        backref=backref('products',
                        uselist=True,
                        cascade='delete,all'))
    user_id = db.Column(db.ForeignKey('user.id'), nullable=False)
    user = relationship(
        User,
        backref=backref('users',
                        uselist=True,
                        cascade='delete,all'))
