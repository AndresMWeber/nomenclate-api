
import os

from flask import Flask
from flask_restful import Api

from resources.nomenclate import Nomenclate, NomenclateList
from resources.token import Token, TokenList

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL',
                                                       'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SECRET_KEY'] = 'andres'
api = Api(app=app)

api.add_resource(Nomenclate, '/nomenclate/<int:_id>')
api.add_resource(NomenclateList, '/nomenclates')
api.add_resource(Token, '/token/<string:name>')
api.add_resource(TokenList, '/tokens')
