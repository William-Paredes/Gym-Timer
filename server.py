from flask import Flask, request
import json 
import time
import const

app = Flask(__name__)


@app.route('/', methods=['PUT', 'GET'])
def messaging():
    if request.method == 'PUT':
        print("hello")
        response = request.get_json(silent=True)
        # open json file update data
        with open(const.data_location, 'w', encoding='utf-8') as outjson:
            json.dump(response, outjson,  indent=4)
            print(response)
        
        return "Okay", 200 

@app.route('/canceltimer', methods=['PUT'])
def cancelTimer():
    if request.method == 'PUT':
        with open(const.data_location, 'r', encoding='utf-8') as outjson:
            json_data = json.load(outjson)
            print(json_data)
            json_data['timer'] = True
    
        with open('data.json', 'w') as output:
            json.dump(json_data, output, indent=4)
        print(json_data)
        return "Canceled"
