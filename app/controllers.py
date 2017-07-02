from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from app.model import User, Drink, Audit
from app.forms import AddUser, AddDrink
from app import app, db

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
        user = User(form.username.data, form.email.data)
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
        user.audit = form.audit.data
        db.session.commit()
        return redirect(url_for('users.get_users'))
    return render_template('form.html', form=form,
        title='Edit User: {}'.format(user.username),
        submit_value='Edit')

buy = Blueprint('buy', __name__, url_prefix='/buy')

@buy.route('/')
def select_user():
    users = User.query.all()
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
        if user.audit:
            audit = Audit(difference=drink.price, drink=drink.id, user=0)
        else:
            audit = Audit(difference=drink.price, drink=drink.id, user=user.id)
        db.session.add(audit)
        db.session.commit()
	flash('Thank you, {}. You have bought {}.'.format(user.username, drink.name), 'success')
    return redirect(url_for('buy.select_user'))

#Drinks
drinks = Blueprint('drinks', __name__, url_prefix='/drinks')

@drinks.route('/', methods = ['GET'])
def get_drinks():
    drinks = Drink.query.all()
    return render_template('drinks.html', drinks = drinks)

@drinks.route('/add', methods = ['GET','POST'])
def add_drink():
    form = AddDrink()
    if form.validate_on_submit():
        drink = Drink(form.name.data, form.bottle_size_l.data,
            form.caffeine_mg.data, form.price.data)
        db.session.add(drink)
        db.session.commit()
        return redirect(url_for('drinks.get_drinks'))
    return render_template('form.html', form=form, 
        title='Add Drink', submit_value='Add')

@drinks.route('/<did>/edit', methods = ['GET','POST'])
def edit_drink(did):
    drink = Drink.query.filter_by(id=did).first()
    form = AddDrink(obj=drink)
    if form.validate_on_submit():
        drink.name = form.name.data
        drink.bottle_size_l = form.bottle_size_l.data
        drink.caffeine_mg = form.caffeine_mg.data
        drink.price = form.price.data
        db.session.commit()
        return redirect(url_for('drinks.get_drinks'))
    return render_template('form.html', form=form,
        title='Edit Drink: {}'.format(drink.name),
        submit_value='Edit')