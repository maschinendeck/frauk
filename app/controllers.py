from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from app.model import User
from app.forms import AddUser
from app import db

users = Blueprint('users', __name__, url_prefix='/users')

@users.route('/', methods = ['GET'])
def get_users():
    users = User.query.all()
    return render_template('users.html', users = users)

@users.route('/add', methods = ['GET','POST'])
def add_user():
    form = AddUser()
    if form.validate_on_submit():
        user = User(form.username.data, form.email.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.get_users'))
    return render_template('add_user.html', form=form)

@users.route('/<uid>/edit', methods = ['GET','POST'])
def edit_user(uid):
    user = User.query.filter_by(id=uid).first()
    form = AddUser(obj=user)
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        db.session.commit()
        return redirect(url_for('users.get_users'))
    return render_template('edit_user.html', form=form)
    
