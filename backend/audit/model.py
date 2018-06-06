import datetime
from backend import db, Base
from ..product.model import Product
from ..user.model import User
from sqlalchemy.orm import (relationship, backref)

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
