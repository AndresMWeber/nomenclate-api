from six import iteritems
import pusher
import os

from nomenclate import Nom
from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow

from models.nomenclate import NomenclateModel
from models.token import TokenModel
from resources.nomenclate import Nomenclate, NomenclateList
from resources.token import Token, TokenList

app = Flask(__name__)
ma = Marshmallow(app)
pusher_client = pusher.Pusher(
  app_id=os.environ['PUSHER_APP_ID'],
  key=os.environ['PUSHER_KEY'],
  secret=os.environ['PUSHER_SECRET'],
  cluster='us2',
  ssl=True
)

app.nomenclate = Nom()

@app.route('/render/<int:_id>')
def render_nomenclate(_id):
    nomenclate = NomenclateModel.find_by_id(_id)
    nomenclate_json = nomenclate.json()
    
    app.nomenclate.format = nomenclate_json.get('format', app.nomenclate.format)

    tokens = nomenclate_json.pop('tokens')
    
    for k, v in iteritems(app.nomenclate.state):
        token = TokenModel.find_by_kwargs(id=nomenclate.id, name=k)
        if token is None:
            #token = TokenModel(**{k: v, 'nomenclate_id': nomenclate.id})
            pass
        token.save_to_db()
    
    for token in tokens:
        nom_token = getattr(app.nomenclate, token.pop('name'))
        for k, v in iteritems(token):
            if hasattr(nom_token, k):
                setattr(nom_token, k, v)
    
    return app.nomenclate.get()


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app=app)

api.add_resource(Nomenclate, '/nomenclate/<int:_id>')
api.add_resource(NomenclateList, '/nomenclates')
api.add_resource(Token, '/token/<string:name>')
api.add_resource(TokenList, '/tokens')
