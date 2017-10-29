from flask import Blueprint, render_template, flash, redirect, url_for
from ..model import User, Money, Audit
from .. import db
from decimal import Decimal
import sqlalchemy

deposit = Blueprint('deposit', __name__, url_prefix='/deposit')

@deposit.route('/')
def select_user():
    users = User.query.order_by(sqlalchemy.func.lower(User.username)).all()
    return render_template('user_selection_deposit.html', users=users)

@deposit.route('/<uid>')
def select_amount(uid):
    user = User.query.get(uid)
    money = [
        { 'name' : '5 Euro', 'amount' : 5.0 },
        { 'name' : '10 Euro', 'amount' : 10.0 },
    ]
    return render_template('money_selection.html', user=user, money=money)

@deposit.route('/<int:uid>/<float:amount>')
def make_deposit(uid, amount):
    user = User.query.get(uid)
    if user and amount:
        user.balance = user.balance + Decimal(amount)
        userid = 0
        if user.audit:
            userid = user.id
        audit = Audit(Decimal(amount), 0, userid)
        db.session.add(audit)
        db.session.commit()
    flash(u'Thank you, {}. Your new balance is {}'.format(user.username, user.balance), 'success')
    return redirect(url_for('deposit.select_user'))
