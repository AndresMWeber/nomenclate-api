from flask_restful import Resource, reqparse
from models.token import TokenModel
from models.nomenclate import NomenclateModel
from six import iteritems

class Token(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)
    parser.add_argument('token', type=str)
    parser.add_argument('label', type=str, default='')
    parser.add_argument('case', type=str, default='')
    parser.add_argument('prefix', type=str, default='')
    parser.add_argument('suffix', type=str, default='')
    parser.add_argument('nomenclate_id', type=int, required=True, help="All tokens need a nomenclate ID")

    @classmethod
    def get(cls, name):
        token = TokenModel.find_by_name(name)
        if token:
            return token.json()
        return {"message": "token not found"}, 404

    def post(self, name):
        if TokenModel.find_by_name(name):
            return {'message': "A token instance with id '{}' already exists".format(name)}, 400
        
        data = self.parser.parse_args()
        data['name'] = name
        data['token'] = data.get('token', name)

        if NomenclateModel.find_by_id(data['nomenclate_id']) is None:
            return {'message': "No Nomenclate object exists at id: %s" % data['nomenclate_id']}

        token = TokenModel(**data)
        try:
            token.save_to_db()
        except:
            return {'message': "An error occurred inserting the token {}.".format(name)}, 500
        return token.json(), 201

    def delete(self, name):
        token = TokenModel.find_by_name(name)
        if token:
            token.delete_from_db()
        return {'message': 'Token "{}" deleted'.format(name)}

    def put(self, name):
        data = self.parser.parse_args()
        data['name'] = name
        data['token'] = data.get('token', name)

        token = TokenModel.find_by_name(name)

        if token is None:
            token = TokenModel(**data)
        else:
            token.instance.merge_serialization(data)

        token.save_to_db()

        return token.json()

    def patch(self, name):
        data = self.parser.parse_args()
        data['name'] = name
        data['token'] = data.get('token', name)

        token = TokenModel.find_by_name(name)

        if token is None:
            return {'message': 'Could not find {}(name={}) in DB'.format(
                self.__class__.__name__, name)}, 404
        else:
            for k, v in iteritems(data):
                if hasattr(token, k):
                    setattr(token, k, v)

        token.save_to_db()

        return token.json()


class TokenList(Resource):
    def get(self):
        return {'tokens': [x.json() for x in TokenModel.find_all()]}
