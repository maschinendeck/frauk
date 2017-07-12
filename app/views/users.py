from flask import Blueprint, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from ..model import User
from ..forms import AddUser
from .. import app, db

#Users
users = Blueprint('users', __name__, url_prefix='/users')

@users.route('/', methods = ['GET'])
def get_users():
    users = User.query.all()
    return render_template('users.html', users = users)

@users.route('/add', methods = ['GET','POST'])
def add_user():
    form = AddUser()
    if form.validate_on_submit():
        if form.logo.data:
            f = form.logo.data
            filename = secure_filename(f.filename)
            f.save(os.path.join(
                app.root_path, 'static', 'uploads', filename))
        else:
            filename = ''
        user = User(form.username.data, form.email.data, filename)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.get_users'))
    return render_template('form.html', form=form, 
        title='Add User', submit_value='Add')

@users.route('/<uid>/edit', methods = ['GET','POST'])
def edit_user(uid):
    user = User.query.filter_by(id=uid).first()
    form = AddUser(obj=user)
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.balance = form.balance.data
        user.audit = form.audit.data
        db.session.commit()
        return redirect(url_for('users.get_users'))
    return render_template('form.html', form=form,
        title='Edit User: {}'.format(user.username),
        submit_value='Edit')
