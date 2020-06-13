from flask import Flask
from flask_restful import Resource, Api
import requests
app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self):
        response = requests.get('http://flask-server:5000/flaskserver')
        return response.json()

api.add_resource(Product, '/flaskclient')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)