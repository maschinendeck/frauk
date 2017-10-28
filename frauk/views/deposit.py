from flask import Blueprint, render_template, flash, redirect, url_for
from ..model import User, Money, Audit
from .. import db
import sqlalchemy

deposit = Blueprint('deposit', __name__, url_prefix='/deposit')

@deposit.route('/')
def select_user():
    users = User.query.order_by(sqlalchemy.func.lower(User.username)).all()
    return render_template('user_selection_deposit.html', users=users)

@deposit.route('/<uid>')
def select_amount(uid):
    user = User.query.get(uid)
    money = Money.query.all()
    return render_template('money_selection.html', user=user, money=money)

@deposit.route('/<uid>/<mid>')
def make_deposit(uid, mid):
    user = User.query.get(uid)
    money = Money.query.get(mid)
    if user and money:
        user.balance = user.balance + money.price
        userid = 0
        if user.audit:
            userid = user.id
        audit = Audit(-1 * money.price, money.id, userid)
        db.session.add(audit)
        db.session.commit()
    flash(u'You have deposited {}. New balance: {}'.format(money.price, user.balance), 'success')
    return redirect(url_for('buy.select_user'))
