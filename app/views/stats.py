from flask import Blueprint, render_template
from ..model import Audit, Drink, User
from app import db
import datetime

stats = Blueprint('stats', __name__, url_prefix='/stats')

@stats.route('/', methods = ['GET'])
def get_stats(uid = None):
    drinks = db.session.query(db.func.count(Audit.drink_id), Drink.name).\
        join(Drink).\
        group_by(Audit.drink_id).\
        order_by(db.desc(db.func.count(Audit.drink_id))).\
        limit(5).all()
    users = db.session.query(db.func.count(Audit.user_id), User.username).\
        join(User).\
        group_by(Audit.user_id).\
        order_by(db.desc(db.func.count(Audit.user_id))).\
        limit(5).all()
    
    startOfMonth = datetime.datetime.now().replace(day=1)
    startOfDay = datetime.datetime.now().replace(hour=0,minute=0,second=0)
    tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)

    caff_month = Audit.query.join(Drink).filter(Audit.created_at > startOfMonth)
    sum_month = sum([c.drink.caffeine_mg * c.drink.bottle_size_l * 10 for c in caff_month])

    caff_day = Audit.query.join(Drink).filter(Audit.created_at > startOfDay)
    sum_day = sum([c.drink.caffeine_mg * c.drink.bottle_size_l * 10 for c in caff_day])

    return render_template('stats.html',
        drinks = drinks,
        users = users,
        caff_month = sum_month,
        caff_day = sum_day)
