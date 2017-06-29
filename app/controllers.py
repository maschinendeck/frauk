import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from app import db
import app.models
import app.forms

users = Blueprint('users', __name__, url_prefix='/users')

@users.route('/new')
# usw

