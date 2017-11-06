import datetime
from frauk import db, ma
from marshmallow import fields

class Audit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    difference = db.Column(db.Integer, default=0)
    product_id = db.Column(db.ForeignKey('product.id'), nullable=False)
    user_id = db.Column(db.ForeignKey('user.id'), nullable=False)

class AuditSchema(ma.ModelSchema):
    class Meta:
        model = Audit
