from six import iteritems
from flask_restful import Resource, reqparse
from models.nomenclate import NomenclateModel
from models.token import TokenModel


class Nomenclate(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('format', type=str, required=True, help="Must specify a format string for the Nomenclate object.")
    
    @classmethod
    def get(cls, _id):
        Nomenclate = NomenclateModel.find_by_id(_id)
        if Nomenclate:
            return Nomenclate.json()
        return {"message": "Nomenclate not found"}, 404

    def post(self, _id):
        if NomenclateModel.find_by_id(_id):
            return {'message': "A nomenclate instance with id '{}' already exists".format(_id)}, 400
        data = self.parser.parse_args()
        nomenclate = NomenclateModel(**data)

        try:
            nomenclate.save_to_db()
        except:
            return {'message': "An error occurred inserting the Nomenclate {}.".format(_id)}, 500
        
        return nomenclate.json(), 201

    def delete(self, _id):
        Nomenclate = NomenclateModel.find_by_id(_id)
        if Nomenclate:
            Nomenclate.delete_from_db()
            return {'message': 'Nomenclate %s deleted' % _id}
        return {'message': 'Nomenclate %s does not exist' % _id}

    def patch(self, _id, **kwargs):
        data = self.parser.parse_args()

        nomenclate = NomenclateModel.find_by_id(_id)

        if nomenclate is None:
            return {'message': 'Could not find {}(id={}}) in DB'.format(
                self.__class__.__name__, _id)}, 404
        else:
            for k, v in iteritems(data):
                if hasattr(nomenclate, k):
                    setattr(nomenclate, k, v)

        nomenclate.save_to_db()

        return nomenclate.json()


class NomenclateList(Resource):
    def get(self):
        return {'nomenclates': [x.json() for x in NomenclateModel.find_all()]}
