from frauk import db
from flask_restful import Resource
from flask import request
from .model import User, UserSchema
from sqlalchemy import update

userSchema = UserSchema()
usersSchema = UserSchema(many=True)

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
