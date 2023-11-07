from flask import Flask, jsonify
from rand_str import information, chemical_formula_information, aspirin_info, information_medicament
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

@app.route('/medicament/<medicament>',methods=['GET'])
def search_medicament(medicament):
    list_comp, list_synonyms = information_medicament(medicament)
    comp_dict = {
        "Compounds" : list_comp ,
        "Synonyms" : list_synonyms
                 }

    return jsonify(comp_dict),200

@app.route('/aspirin')
def aspirin():
    response = aspirin_info()
    return jsonify(response), 200

@app.route('/chemical/<chemical_formula>',methods=['GET'])
def chemical_formula_get(chemical_formula):
    response = chemical_formula_information(chemical_formula)
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=5000)
