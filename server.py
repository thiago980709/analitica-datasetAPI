from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers.DataSet import DataSet

app = Flask(__name__)
CORS(app)

@app.route("/dataSet", methods=['GET'])
def getAll():
    return (DataSet.list())

@app.route("/dataSet", methods=['POST'])
def postOne():
    body = request.json
    return (DataSet.create(body))

@app.route("/dataSet/delete/<id>", methods=['DELETE'])
def deleteOne(id):
    body = request.json
    return (DataSet.delete(id))

@app.route("/dataSet/update/<id>/<encargado>", methods=['PUT'])
def updateEncargado(id,encargado):
    body = request.json
    return (DataSet.updateEncargado(id,encargado))

@app.route("/dataSet/updateFile", methods=['PUT'])
def updateArchivo():
    body = request.json
    return (DataSet.updateArchivo(body))

