from flask import Blueprint, render_template
from ..model import Audit

audits = Blueprint('audits', __name__, url_prefix='/audits')

@audits.route('/', methods = ['GET'])
@audits.route('/<uid>', methods = ['GET'])
def get_audits(uid = None):
    audits = Audit.query.join('drink').outerjoin('user')
    if uid:
        # this filters on the last joined table. therefore id is User.id
        audits = audits.filter_by(id=uid)
    return render_template('audits.html', query = audits.paginate())
