from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from app.model import User
#import app.forms

users = Blueprint('users', __name__, url_prefix='/users')

@users.route('/', methods = ['GET'])
def get_users():
    users = User.query.all()
    return render_template('users.html', users = users)

