import graphene
import datetime
from backend import db
from .model import User
from .schema import UserSchema


class ModifyUserInput(graphene.InputObjectType):
    user_id = graphene.Int(required=True)
    name = graphene.String()
    email = graphene.String()
    audit = graphene.Boolean()
    active = graphene.Boolean()

class ModifyUser(graphene.Mutation):
    class Arguments:
        user_data = ModifyUserInput()
    
    ok = graphene.Boolean()
    user = graphene.Field(lambda : UserSchema)

    def mutate(self, info, user_data=None):
        if user_data:
            user = User.query.filter_by(id=user_data.user_id).first()
            if user == None:
                return ModifyUser(user=user, ok=False)
            changed = False
            if "name" in user_data:
                user.name = user_data.name
                changed = True
            if "email" in user_data:
                user.email = user_data.email
                changed = True
            if "audit" in user_data:
                user.audit = user_data.audit
                changed = True
            if "active" in user_data:
                user.active = user_data.active
                changed = True
            if changed:
                user.updated_at = datetime.datetime.now()
                db.session.add(user)
                db.session.commit()
                ok = True
                return ModifyUser(user=user, ok=ok)
            else:
                ok = False
                return ModifyUser(user=user, ok=ok)

class CreateUserInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    email = graphene.String()
    audit = graphene.Boolean()
    active = graphene.Boolean()

class CreateUser(graphene.Mutation):
    class Arguments:
        user_data = CreateUserInput()

    ok = graphene.Boolean()
    user = graphene.Field(lambda: UserSchema)

    def mutate(self, info, user_data=None):
        if user_data:
            user = User(name=user_data.name)
            if "email" in user_data:
                user.email = user_data.email
            if "audit" in user_data:
                user.audit = user_data.audit
            if "active" in user_data:
                user.active = user_data.active
            db.session.add(user)
            db.session.commit()
            ok = True
            return CreateUser(user=user, ok=ok)
        else:
            return CreateUser(user=None, ok=False)
