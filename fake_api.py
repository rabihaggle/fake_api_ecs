from flask import Flask, jsonify
from rand_str import information
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

@app.route('/random_word/<random_word>',methods=['GET'])
def random_string(random_word):
    str_ran = information(random_word)
    return str_ran

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=5000)
