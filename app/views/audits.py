from flask import Blueprint, render_template
from ..model import Audit

audits = Blueprint('audits', __name__, url_prefix='/audits')

@audits.route('/', methods = ['GET'])
def get_audits():
    audits = Audit.query.all()
    return render_template('audits.html', audits = audits)
