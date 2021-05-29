from flask import Flask, request, render_template
from flask_restful import Resource, Api
import format_csv
from pymongo import MongoClient
import os

app = Flask(__name__)
api = Api(app)

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.tododb

class listAll(Resource):
    def get(self, dtype='json'):
        topk = request.args.get('top', default=-1, type=int)
        if dtype == 'csv':
            return render_template("display.html", x=format_csv.csv_form(db, topk))
        return render_template("display.html", x=format_csv.json_form(db, topk))

class listOpen(Resource):
    def get(self, dtype='json'):
        topk = request.args.get('top', default=-1, type=int)
        if dtype == 'csv':
            return render_template("display.html", x=format_csv.csv_form(db, topk, "open"))
        return render_template("display.html", x=format_csv.json_form(db, topk, "open"))

class listClose(Resource):
    def get(self, dtype='json'):
        topk = request.args.get('top', default=-1, type=int)
        if dtype == 'csv':
            return render_template("display.html", x=format_csv.csv_form(db, topk, "close"))
        return render_template("display.html", x=format_csv.json_form(db, topk, "close"))

api.add_resource(listAll, '/listAll', '/listAll/<string:dtype>')
api.add_resource(listOpen, '/listOpen', '/listOpen/<string:dtype>')
api.add_resource(listClose, '/listClose', '/listClose/<string:dtype>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)