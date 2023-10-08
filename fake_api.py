from flask import Flask, jsonify

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

if __name__ == '__main__':
    app.run(debug=True,port=8080)
