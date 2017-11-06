import datetime
from frauk import db, ma
from marshmallow import fields

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True)
    email = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())
    balance = db.Column(db.Integer, default=0)
    active = db.Column(db.Boolean, default=True)
    audit = db.Column(db.Boolean, default=True)

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
    name = fields.String(required=True)
    email = fields.Email()
