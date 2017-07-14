from flask import Blueprint, render_template
from ..model import Audit

audits = Blueprint('audits', __name__, url_prefix='/audits')

@audits.route('/', methods = ['GET'])
@audits.route('/<uid>', methods = ['GET'])
def get_audits(uid = None):
    if uid:
        audits = Audit.query.filter_by(user=uid)
    else:
        audits = Audit.query.all()
    return render_template('audits.html', audits = audits)
