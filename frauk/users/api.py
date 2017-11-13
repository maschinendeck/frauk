from frauk import db
from flask_restful import Resource
from flask import request
from .model import User, UserSchema
from frauk.products.model import Product
from frauk.audits.model import Audit, AuditSchema
from sqlalchemy import update

userSchema = UserSchema()
usersSchema = UserSchema(many=True)
auditSchema = AuditSchema()

class UserAPI(Resource):

    def get(self, id):
        user = User.query.get(id)
        return userSchema.dump(user).data

    def delete(self, id):
        user = User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return {}
        else:
            return {}, 404

    def patch(self, id):
        data = request.get_json()
        errors = userSchema.load(data, partial=True).errors
        if errors:
            return errors, 400
        else:
            ex = update(User.__table__).where(User.id == id).values(data)
            db.session.execute(ex)
            db.session.commit()
            return self.get(id)
        
        

class UsersAPI(Resource):

    def get(self):
        users = User.query.all()
        return usersSchema.dump(users).data

    def post(self):
        user = userSchema.load(request.get_json())
        if user.errors:
            return user.errors
        else:
            db.session.add(user.data)
            db.session.commit()
            return userSchema.dump(user.data)

class UserPaymentAPI(Resource):

    def post(self, id):
        amount = request.get_json()
        if isinstance(amount, int):
            if request.path.endswith('pay.json'):
                amount = amount * -1
            user = User.query.get(id)
            if user:
                old_balance = user.balance
                ex = update(User.__table__).where(User.id == id) \
                    .values({ 'balance' : old_balance + amount})
                db.session.execute(ex)
                db.session.commit()
                return {}
            else:
                return {}, 404
        else:
            return {}, 400

class UserTradeAPI(Resource):

    def post(self,id):
        product_id = request.get_json()
        product = Product.query.get(product_id)
        user = User.query.get(id)
        if not product or not user:
            return {}, 404
        audit = auditSchema.load({'difference' : product.price, 'product' : product.id, 'user' : user.id })
        if audit.errors:
            return audit.errors
        db.session.add(audit.data)
        ex = update(User.__table__).where(User.id == id) \
            .values({ 'balance' : user.balance - product.price})
        db.session.execute(ex)
        db.session.commit()
        return 200
