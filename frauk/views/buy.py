from flask import Blueprint, render_template, flash, redirect, url_for
from ..model import User, Item, Audit
from .. import db
import sqlalchemy

buy = Blueprint('buy', __name__, url_prefix='/buy')

@buy.route('/')
def select_user():
    users = User.query.order_by(sqlalchemy.func.lower(User.username)).all()
    return render_template('user_selection.html', users=users)

@buy.route('/<uid>')
def select_item(uid):
    user = User.query.get(uid)
    items = Item.query.all()
    return render_template('item_selection.html', user=user, items=items)

@buy.route('/<uid>/<iid>')
def make_purchase(uid, iid):
    user = User.query.get(uid)
    item = Item.query.get(iid)
    if user and item:
        user.balance = user.balance - item.price
        userid = 0
        if user.audit:
            userid = user.id
        audit = Audit(-1 * item.price, item.id, userid)
        db.session.add(audit)
        db.session.commit()
	flash(u'Thank you, {}. You have bought {} for {}. Your new balance is {}.'.format(\
        user.username, 
        item.name, 
        '{0:0.2f} EUR'.format(item.price), 
        '{0:0.2f} EUR'.format(user.balance)
    ), 'success')
    return redirect(url_for('buy.select_user'))
