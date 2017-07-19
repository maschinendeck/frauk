from flask import Blueprint, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from ..model import User
from ..forms import AddUser, EditUser
from .. import app, db
import sqlalchemy

#Users
users = Blueprint('users', __name__, url_prefix='/users')

@users.route('/', methods = ['GET'])
def get_users():
    users = User.query.order_by(sqlalchemy.func.lower(User.username)).all()
    return render_template('users.html', users = users)

@users.route('/add', methods = ['GET','POST'])
def add_user():
    form = AddUser()
    if form.validate_on_submit():
        user = User()
        user.fromForm(form)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.get_users'))
    return render_template('form.html', form=form, 
        title='Add User', submit_value='Add')

@users.route('/<uid>/edit', methods = ['GET','POST'])
def edit_user(uid):
    user = User.query.filter_by(id=uid).first()
    form = EditUser(obj=user)
    if form.validate_on_submit():
        user.fromForm(form)
        db.session.commit()
        return redirect(url_for('users.get_users'))
    return render_template('form.html', form=form,
        title='Edit User: {}'.format(user.username),
        submit_value='Edit')
