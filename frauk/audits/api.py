from frauk import db
from flask_restful import Resource
from flask import request
from .model import Audit, AuditSchema
from sqlalchemy import func

auditsSchema = AuditSchema(many=True)

class AuditsAPI(Resource):

    def get(self):
        audits = Audit.query.all()
        total_sum = db.session.query(func.sum(Audit.difference).label('sum')).first()[0]
        payments_sum = db.session.query(func.sum(Audit.difference).label('sum')) \
                        .filter(Audit.difference < 0).first()[0]
        deposits_sum = db.session.query(func.sum(Audit.difference).label('sum')) \
                        .filter(Audit.difference > 0).first()[0]
        res = { 'sum' : total_sum,
                'payments_sum' : payments_sum,
                'deposits_sum' : deposits_sum,
                'audits' : auditsSchema.dump(audits).data }
        return res
