from flask import Blueprint, render_template, request
from ..model import Audit

audits = Blueprint('audits', __name__, url_prefix='/audits')

@audits.route('/', methods = ['GET'])
def get_audits():
    audits = Audit.query
    if request.args.get('user'):
        audits = audits.filter_by(user_id=request.args.get('user'))
    if request.args.get('drink'):
        audits = audits.filter_by(drink_id=request.args.get('drink'))
        
    return render_template('audits.html', query = audits.paginate())
