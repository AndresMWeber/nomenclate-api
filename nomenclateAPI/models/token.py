from nomenclate import Nom
from .common import CommonMixin
from db import db


class TokenModel(CommonMixin, db.Model):
    __tablename__ = 'tokens'

    serial_attrs = ['id',
                    'name',
                    'token',
                    'label',
                    'case',
                    'prefix',
                    'suffix',
                    'nomenclate_id']

    name = db.Column(db.String(20))
    token = db.Column(db.String(20))
    label = db.Column(db.String(20))
    case = db.Column(db.String(10))
    prefix = db.Column(db.String(20))
    suffix = db.Column(db.String(20))
    nomenclate_id = db.Column(db.Integer, db.ForeignKey('nomenclates.id'))

    def __init__(self, name, token, label, case, prefix, suffix, nomenclate_id):
        self.name = name
        self.token = token
        self.label = label
        self.case = case
        self.prefix = prefix
        self.suffix = suffix
        self.nomenclate_id = nomenclate_id
