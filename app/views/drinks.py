from flask import Blueprint, render_template, redirect, url_for
from ..model import Drink
from ..forms import AddDrink
from .. import db

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
        drink = Drink()
        drink.fromForm(form)
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
        drink.fromForm(form)
        db.session.commit()
        return redirect(url_for('drinks.get_drinks'))
    return render_template('form.html', form=form,
        title=u'Edit Drink: {}'.format(drink.name),
        submit_value='Edit')
