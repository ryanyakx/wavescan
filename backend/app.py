from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import os

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/validate", methods=["POST"])
@cross_origin()
def validate():
    data = request.get_json()

    projectName = str(data["projectName"])
    scanningMode = str(data["scanningMode"])
    scanDimensionsX = int(data["scanDimensionsX"])
    scanDimensionsY = int(data["scanDimensionsY"])
    scannerFrequency = round(float(data["scannerFrequency"]), 1)

    status = ""
    scanningModeSet = {"GANTRY", "CRAWLER", "AUTO", "MANUAL", "ARM"}

    #projectName has to be more than 3 characters
    if len(projectName) <= 3:
        status += "Project name has to be more than 3 characters!\n"
    
    #Accepted input only
    if scanningMode not in scanningModeSet:
        status += "Invalid scanning mode!\n"

    #Dimension x has to be >= 1
    if scanDimensionsX < 1:
        status += "Dimension X has to be larger than 1!\n"

    #Dimension y has to be >= 1
    if scanDimensionsY < 1:
        status += "Dimension Y has to be larger than 1!\n"

    #Scanner frequency has to be >= 1
    if scannerFrequency < 1:
        status += "Scanner frequency has to be larger than 1!\n"
    
    if status == "":
        return jsonify(
            {
                "code": 200,
                "message": "OK"
            }
        ), 200
    else:
        return jsonify(
            {
                "code": 400,
                "message": status
            }   
        ), 400

@app.route("/success")  
@cross_origin()
def success():
    return jsonify(
        {
            "link": "https://drive.google.com/uc?export=view&id=1dmtW4Rxx8aHNL2DxlXkxNnOONOiYhRO9"
        }
    )
