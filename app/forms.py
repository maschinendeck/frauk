from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Email

class AddDrink(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    bottle_size_l =  FloatField('Bottle Size', validators=[DataRequired()])
    caffeine_mg = IntegerField('Caffeine', validators=[DataRequired()])
    price =  FloatField('Price', validators=[DataRequired()])
    #logo_file_name = StringField('Logo', validators=[DataRequired()])
    #active = BooleanField('Active', validators=[DataRequired()])

class AddUser(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    audit = BooleanField('Appear in Audits')
