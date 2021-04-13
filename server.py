from flask import Flask, request
import json 
import time

app = Flask(__name__)


@app.route('/', methods=['PUT', 'GET'])
def messaging():
    if request.method == 'PUT':
        print("hello")
        response = request.get_json(silent=True)
        # open json file update data
        with open('data.json', 'w', encoding='utf-8') as outjson:
            json.dump(response, outjson,  indent=4)
            print(response)
        return response, 200 
        
