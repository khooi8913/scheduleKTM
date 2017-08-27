from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from trains import display_available_trains

app = Flask(__name__)
api = Api(app)

# def abort_if_todo_doesnt_exist(todo_id):
#     if todo_id not in TODOS:
#         abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('date')
parser.add_argument('origin')
parser.add_argument('destination')

class KTM(Resource):
    def get(self):
    	args = parser.parse_args()
    	return display_available_trains(args['origin'],args['destination'],args['date'])

api.add_resource(KTM, '/')

if __name__ == '__main__':
    app.run(debug=True)