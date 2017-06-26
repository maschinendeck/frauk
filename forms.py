from flask_wtf import Form
from wtforms import StringField, FloatField, IntegerField, BooleanField
from wtforms.validators import DataRequired

class AddDrink(Form):
    name = StringField('Name', validators=[DataRequired()])
    bottle_size =  FloatField('Bottle Size', validators=[DataRequired()])
    caffeine = IntegerField('Caffeine', validators=[DataRequired()])
    price =  FloatField('Price', validators=[DataRequired()])
    logo_file_name = StringField('Logo', validators=[DataRequired()])
    #active = BooleanField('Active', validators=[DataRequired()])

class AddUser(Form):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('E-Mail', validators=[DataRequired()])
    audit = BooleanField('Appear in Audits')
