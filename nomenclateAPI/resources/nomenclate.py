from flask_restful import Resource, reqparse
from models.nomenclate import NomenclateModel


class Nomenclate(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('format', type=str)
    
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
        Nomenclate = NomenclateModel(**data)
        try:
            Nomenclate.save_to_db()
        except:
            return {'message': "An error occurred inserting the Nomenclate {}.".format(_id)}, 500
        return Nomenclate.json(), 201

    def delete(self, _id):
        Nomenclate = NomenclateModel.find_by_id(_id)
        if Nomenclate:
            Nomenclate.delete_from_db()
        return {'message': 'Nomenclate %s deleted' % _id}

    def put(self, _id):
        data = self.parser.parse_args()

        Nomenclate = NomenclateModel.find_by_id(_id)

        if Nomenclate is None:
            Nomenclate = NomenclateModel(**data)
        else:
            Nomenclate.instance.merge_serialization(data)

        Nomenclate.save_to_db()

        return Nomenclate.json()

    def update(self, _id):
        data = self.parser.parse_args()

        Nomenclate = NomenclateModel.find_by_id(_id)

        if Nomenclate is None:
            return {'message': 'Could not find {}(id={}}) in DB'.format(
                self.__class__.__name__, _id)}, 404
        else:
            Nomenclate.instance.merge_serialization(data)

        Nomenclate.save_to_db()

        return Nomenclate.json()


class NomenclateList(Resource):
    def get(self):
        return {'nomenclates': [x.json() for x in NomenclateModel.find_all()]}
