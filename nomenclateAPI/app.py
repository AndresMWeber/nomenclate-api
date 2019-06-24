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
print(app.nomenclate)

@app.route('/render/<int:_id>')
def render_nomenclate(_id):
    nomenclate = NomenclateModel.find_by_id(_id)
    
    app.nomenclate.format = nomenclate.format or app.nomenclate.format
    cur_state = app.nomenclate.state
    print(repr(app.nomenclate))
    print(app.nomenclate.format)
    print(app.nomenclate.tokens)
    print(app.nomenclate.state)
    
    for token in TokenModel.find_all_by_id(nomenclate.id):
        print(token.json())
        if cur_state.get(token.name) and hasattr(app.nomenclate, token.name):
            nomenclate_token = getattr(app.nomenclate, token.name)
            for k, v in iteritems(token.json()):
                if hasattr(nomenclate_token, k) and not k == 'name':
                    setattr(nomenclate_token, k, v or "")
    
    print(repr(app.nomenclate))
    print(app.nomenclate.format)
    print(app.nomenclate.tokens)
    print(app.nomenclate.state)
    return app.nomenclate.get()


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app=app)

api.add_resource(Nomenclate, '/nomenclate/<int:_id>')
api.add_resource(NomenclateList, '/nomenclates')
api.add_resource(Token, '/token/<string:name>')
api.add_resource(TokenList, '/tokens')
