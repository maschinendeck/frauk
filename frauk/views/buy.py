from flask import Blueprint, render_template, flash, redirect, url_for
from ..model import User, Drink, Audit
from .. import db
import sqlalchemy

buy = Blueprint('buy', __name__, url_prefix='/buy')

@buy.route('/')
def select_user():
    users = User.query.order_by(sqlalchemy.func.lower(User.username)).all()
    return render_template('user_selection.html', users=users)

@buy.route('/<uid>')
def select_drink(uid):
    user = User.query.get(uid)
    drinks = Drink.query.all()
    return render_template('drink_selection.html', user=user, drinks=drinks)

@buy.route('/<uid>/<did>')
def make_purchase(uid, did):
    user = User.query.get(uid)
    drink = Drink.query.get(did)
    if user and drink:
        user.balance = user.balance - drink.price
        userid = 0
        if user.audit:
            userid = user.id
        audit = Audit(-1 * drink.price, drink.id, userid)
        db.session.add(audit)
        db.session.commit()
	flash(u'Thank you, {}. You have bought {} for {}. Your new balance is {}.'.format(\
        user.username, 
        drink.name, 
        '{0:0.2f} EUR'.format(drink.price), 
        '{0:0.2f} EUR'.format(user.balance)
    ), 'success')
    return redirect(url_for('buy.select_user'))