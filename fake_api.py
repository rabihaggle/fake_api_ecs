from flask import Flask, jsonify
from chemical import chemical_information
app = Flask(__name__)

@app.route('/')
def hello_world():
    response = {
        'message': 'Hello, World!'
    }
    return jsonify(response), 200

@app.route('/database')
def database_status():
    response = {
        'message': 'Database OK'
    }
    return jsonify(response), 200

@app.route('/chemical')
def chemical():
    response = chemical_information()
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=5000)
