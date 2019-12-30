# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 11:11:11 2019

@author: Mitch

Will launch a server on port 5000.
Endpoints:
 GET: /
 GET: /json
 GET: /name/<name>
"""

from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    # Return format is output: (data, status code)
    return 'Hello world!'

@app.route('/json', methods=['GET'])
def hello_json():
    """Returns data in JSON format. By default, dicts returned
    as response data will be transformed to JSON"""
    payload = {
        'message': 'Hello',
        'recipient': 'World'
    }

    return payload, 200

@app.route('/name/<name>', methods=['GET'])
def hello_name(name):
    """Demonstrates taking a URI parameter from the request.
    For instance, a request to /name/abby will return {'message': 'Hello', 'recipient': 'abby'}"""
    payload = {
        'message': 'Hello',
        'recipient': name
    }
    return payload, 200

if __name__ == '__main__':
    app.run()
    
        