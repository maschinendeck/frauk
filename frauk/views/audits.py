from flask import Blueprint, render_template, request, jsonify
from ..model import Audit

audits = Blueprint('audits', __name__, url_prefix='/audits')

@audits.route('/', methods = ['GET'])
@audits.route('.json', methods = ['GET'])
def get_audits():
    audits = Audit.query
    if request.args.get('user'):
        audits = audits.filter_by(user_id=request.args.get('user'))
    if request.args.get('drink'):
        audits = audits.filter_by(drink_id=request.args.get('drink'))

    if request.path.endswith('.json'):
        result = [{
            'created_at'    : a.created_at,
            'difference'    : a.difference,
            'drink_id'      : a.drink_id,
            'user_id'       : a.user_id,
        } for a in audits.all()]
        return jsonify(result);
        
    return render_template('audits.html', query = audits.paginate())
