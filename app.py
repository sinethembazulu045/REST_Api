import flask
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource, reqparse
import os


app =flask.Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URL'] = 'postgresql://user:pass@localhost/sqlachemy'+ os.path.join(basedir, 'postgres.postgresql')

api = Api(app)

Computers = [
    {
        "id" : 1,
        "computer_name" : "ACER",
        "hpard_drive" : "HDD for Acer Aspire 5051",
        "processor" : "Intel Core i5 processor",
        "amount_of_ram" : '4GB',
        "maximum_ram" : '8GB',
        "hard_drive_space" : "500GB",
        "form_factor" : "20 cm"
    },
     {
         "id" :2,
        "computer_name" : "ASUS X541sa",
        "hard_drive" : "Intel Dual Core N2060",
        "processor" : "Intel core i7 processor",
        "amount_of_ram" : "6GB",
        "maximum_ram" : "8GB",
        "hard_drive_space" : "500GB",
        "form_factor" : "45 cm"
    }
]
 
class Computer_api(Resource):
    def get(self, name): # READ
        for Computer in Computers:
            if(name == Computer["computer_name"]):
                return Computer,200
        return "Computer not found" ,404


    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    @app.route('/', methods=['GET'])
    def home():
        return '''<h1>Computers</h1>
        <p>A prototype API for Umuzi Computers.</p>'''

    @app.route('/api/v1/resources/Computers/all', methods=['GET'])
    def api_all(): 
        conn = sqlite3.connect('Computers.db')
        conn.row_factory = dict_factory
        cur = conn.cursor()
        all_Computers = cur.execute('SELECT * FROM Computers;').fetchall()

        return jsonify(all_Computers)

    def read():
        # list of all computers
        return [Computers[key] for key in sorted(Computer.keys())]

    def post(self, name): # Create
        parser  = reqparse.RequestParser()
        parser.add_argument("hard_drive")
        parser.add_argument("processor")
        parser.add_argument("amount_of_ram")
        parser.add_argument("maximum_ram")
        parser.add_argument("hard_drive_space")
        parser.add_argument("form_factor")
        args = parser.parse_args()


        for Computer in Computers:
             if(name == computer["computer_name"]):
                Computer["hard_drive"] = args["hard_drive"]
                Computer["processor"] = args["processor"]
                Computer["ram_amount"] = args["ram_amount"]
                Computer["maximum_ram"] = args["maximum_ram"]
                Computer["hard_drive_space"] = args["hard_drive_space"]
                Computer["form_factor"] = args["form_factor"]
                return Computer, 200

        Computer = {
            "computer_name" : name,
            "hard_drive" : args["hard_drive"],
            "processor" : args["processor"],
            "ram_amount" : args["ram_amount"],
            "maximum_ram" : args["maximum_ram"],
            "hard_drive_space" : args["hard_drive_space"],
            "form_factor" : args["form_factor"]
        }
        Computers.append(computer)
        return computer, 201

    def put(self, name): # Update
        parser  = reqparse.RequestParser()
        parser.add_argument("hard_drive")
        parser.add_argument("processor")
        parser.add_argument("ram_amount")
        parser.add_argument("maximum_ram")
        parser.add_argument("hard_drive_space")
        parser.add_argument("form_factor")
        args = parser.parse_args()


        for Computer in Computers:
            if(name == computer["computer_name"]):
                Computer["hard_drive"] = args["hard_drive"]
                Computer["processor"] = args["processor"]
                Computer["ram_amount"] = args["ram_amount"]
                Computer["maximum_ram"] = args["maximum_ram"]
                Computer["hard_drive_space"] = args["hard_drive_space"]
                Computer["form_factor"] = args["form_factor"]
                return computer, 200

        Computer = {
            "computer_name" : name,
             "hard_drive" : args["hard_drive"],
             "processor" : args["processor"],
             "ram_amount" : args["ram_amount"],
             "maximum_ram" : args["maximum_ram"],
             "hard_drive_space" : args["hard_drive_space"],
             "form_factor" : args["form_factor"]
        }
        Computers.append(Computer)
        return Computer, 201

    def delete(self, name): # Delete
        global Computers
        Computers = [Computer for Computer in Computers if Computer["computer_name"] != name]
        return "<h1>404</h1><p>The resource could not be found.</p>", 404

    @app.route('/api/v1/resources/computer', methods=['GET'])
    def api_id():
        if 'id' in request.args:
            id = int(request.args['id'])
        else:
            return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
        results = []

        for Computer in Computers:
            if Computer['id'] == id:
                results.append(Computer)
        return jsonify(results)

app.run()
api.add_resource(Computer_api, "/computer/<string:name>")
app.run(debug=True)
