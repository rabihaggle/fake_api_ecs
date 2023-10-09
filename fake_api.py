from flask import Flask, jsonify
from conn_mysql import checkstatusbd
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Access environment variables
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

@app.route('/')
def hello_world():
    response = {
        'message': 'Hello, World!'
    }
    return jsonify(response), 200

@app.route('/database',methods=['GET'])
def database_status():
    ret, exp = checkstatusbd(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME)
    if ret:
        return jsonify({"status":ret,"message":"Mysql OK"}),200
    else:
        return jsonify({"status":ret,"message":"Mysql ERROR","Exception": exp}),500

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=5000)
