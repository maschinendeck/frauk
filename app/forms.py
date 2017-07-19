from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, FloatField, IntegerField, \
    BooleanField, SubmitField
from flask_wtf.file import FileField
from wtforms.validators import DataRequired, Email, Optional, Regexp
from app.validators import ImageValidator, UniqueValidator
from app.model import User

class AddDrink(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    bottle_size_l =  FloatField('Bottle Size', validators=[DataRequired()])
    caffeine_mg = IntegerField('Caffeine', validators=[DataRequired()])
    price =  DecimalField('Price', validators=[DataRequired()], places=2)
    submit = SubmitField('Submit')

class EditUser(FlaskForm):
    username = StringField('Name', validators=[
        DataRequired(),
        Regexp("^\w+$", message = 'Username is alphanumeric only')
    ])
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    balance = DecimalField('Balance', validators=[DataRequired()], places=2)
    audit = BooleanField('Appear in Audits')
    submit = SubmitField('Submit')

class AddUser(FlaskForm):
    username = StringField('Name', validators=[
        DataRequired(),
        Regexp("^\w+$", message = 'Username is alphanumeric only'),
        UniqueValidator(User, User.username)
    ])
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    balance = DecimalField('Balance', validators=[DataRequired()], places=2)
    audit = BooleanField('Appear in Audits')
    submit = SubmitField('Submit')
