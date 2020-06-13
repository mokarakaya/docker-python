from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self):
        return {'products': ['product1', 'product2']}

api.add_resource(Product, '/flaskserver')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)