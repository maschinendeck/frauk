from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for
from werkzeug.utils import secure_filename
import os
    

from app.model import User, Drink, Audit
from app.forms import AddUser, AddDrink
from app import app, db


@app.route("/")
def site_map():
    def has_no_empty_params(rule):
        defaults = rule.defaults if rule.defaults is not None else ()
        arguments = rule.arguments if rule.arguments is not None else ()
        return len(defaults) >= len(arguments)
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    # links is now a list of url, endpoint tuples
    from flask import render_template_string
    tmpl="""
    <html>
        <head><title>list of endpoints for debugging</title></head>
        <body><h1>frauk</h1><h2>list of endpoints</h2>
        <ul>
        {% for route in routes %}
            <li>
            <a href="{{route[0]}}">{{route[1]}} ({{route[0]}})</a>
            </li>
        {% endfor %}
        </ul>
    </html>
    """
    return render_template_string(tmpl, routes=links)



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
	flash('Thank you, {}. You have bought {} for {}. Your new balance is {}.'.format(\
        user.username, 
        drink.name, 
        '{0:0.2f} EUR'.format(drink.price), 
        '{0:0.2f} EUR'.format(user.balance)
    ), 'success')
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
