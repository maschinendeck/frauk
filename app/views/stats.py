from flask import Blueprint, render_template
from ..model import Audit, Drink, User
from app import db

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
    return render_template('stats.html', drinks = drinks, users = users)
