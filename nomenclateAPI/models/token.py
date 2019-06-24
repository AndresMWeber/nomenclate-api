from nomenclate import Nom
from .common import CommonMixin
from models.nomenclate import NomenclateModel
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
