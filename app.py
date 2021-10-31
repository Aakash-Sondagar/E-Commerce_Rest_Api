from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, abort, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class Productmodel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(45), nullable=True)
    name = db.Column(db.String(15), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'ECommerce(name = {self.name}, price = {self.price})'


db.create_all()

put_args = reqparse.RequestParser()
put_args.add_argument('description', type=str, help='description of the Product', required=False)
put_args.add_argument('name', type=str, help='Name of the Product', required=True)
put_args.add_argument('price', type=str, help='price of the Product', required=True)

update_args = reqparse.RequestParser()
update_args.add_argument('description', type=str, help='description of the Product')
update_args.add_argument('name', type=str, help='Name of the Product')
update_args.add_argument('price', type=str, help='price of the Product')

resource_field = {
    'id': fields.Integer,
    'description': fields.String,
    'name': fields.String,
    'price': fields.String
}


class ECommerce(Resource):

    @marshal_with(resource_field)
    def get(self, id):
        result = Productmodel.query.filter_by(id=id).first()
        if not result:
            abort(404, message='Invalid Product ID...')
        return result

    @marshal_with(resource_field)
    def put(self, id):
        args = put_args.parse_args()
        result = Productmodel.query.filter_by(id=id).first()
        if result:
            abort(409, message='Product id is taken...')
        product = Productmodel(id=id, name=args['name'], description=args['description'], price=args['price'])
        db.session.add(product)
        db.session.commit()
        return product, 201

    @marshal_with(resource_field)
    def patch(self, id):
        args = update_args.parse_args()
        result = Productmodel.query.filter_by(id=id).first()
        if not result:
            abort(404, message='Coin does not exist,cannot update...')

        if args['name']:
            result.name = args['name']
        if args['description']:
            result.description = args['description']
        if args['price']:
            result.price = args['price']

        db.session.commit()
        return result

    def delete(self, id):
        result = Productmodel.query.filter_by(id=id).first()
        if not result:
            abort(404, message='Invalid Product ID...')
        Productmodel.query.filter_by(id=id).delete()
        db.session.commit()
        return '', 204


Product = {0: {'Apple': 15},
           1: {'Mango': 17},
           2: {'Orange': 21}
           }
Order_Dic = {}


class Order(Resource):
    def get(self, order_id):
        result = Order_Dic[order_id]
        if not order_id in Order_Dic.keys():
            abort(404, message='Invalid Order ID...')
        return result

    def put(self, order_id):
        args = put_args.parse_args()
        if order_id in Order_Dic.keys():
            abort(409, message='Order id is taken...')
        order = {'name': args['name'], 'price': args['price']}
        Order_Dic[order_id] = order
        return order, 201

    def patch(self, order_id):
        args = update_args.parse_args()
        result = Order_Dic[order_id]
        if not order_id in Order_Dic.keys():
            abort(404, message='Order does not exist,cannot update...')

        if args['name']:
            result['name'] = args['name']
        if args['price']:
            result['price'] = args['price']

        return result

    def delete(self, order_id):
        if order_id in Order_Dic.keys():
            result = Order_Dic.pop(order_id, 'No Key found')
            return result, 204
        else:
            abort(404, message='Invalid Order ID...')


api.add_resource(ECommerce, '/product/<int:id>')
api.add_resource(Order, '/order/<int:order_id>')

if __name__ == '__main__':
    app.run(debug=True)
