from nomenclate import Nom
from .common import CommonMixin
from db import db


class NomenclateModel(CommonMixin, db.Model):
    __tablename__ = 'nomenclates'

    serial_attrs = ['id', 'format', 'tokens']

    format = db.Column(db.String(80))
    tokens = db.relationship('TokenModel', lazy='dynamic')

    def __init__(self, format):
        self.format = format

    def json(self):
        json_repr = super(NomenclateModel, self).json()
        json_repr['tokens'] = [token.json() for token in self.tokens.all()]
        return json_repr
