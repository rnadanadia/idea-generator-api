import os
import json

from flask import Flask, request, jsonify


from utils.preprocessing import Preprocessing
from utils.idea_generator import Generator


app = Flask(__name__)
app.env = 'development'

@app.route('/api/home', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome Idea Generator!'})

@app.route('/api/idea_generator', methods=['GET'])
def get_idea():
    if(os.path.isfile("./data/body.json")):
        with open("./data/body.json", "r") as read_file:
            body = json.load(read_file)
            return jsonify(body), 200
    else:
        return jsonify({'message': 'No body file not exist!'}),400
    

@app.route('/api/idea_generator', methods=['POST'])
def create_idea():
    data = request.get_json()
    raw_question = data['question']
    quantity = data['quantity']
    enhaced = data['enhaced']
    workshop_method = data['workshop_method']

    prepocessing = Preprocessing(input_data=raw_question)
    if (prepocessing.prepare_question()):
        prepered_question = prepocessing.output_data
        generator = Generator(question=prepered_question, number_of_idea=quantity, enhaced=enhaced, workshop_method=workshop_method)
        if (generator.generate_idea()):
            if (enhaced):
                idea_list = generator.idea_list_enhaced
                return jsonify({'idea_list': idea_list}), 200
            else:
                idea_list = generator.idea_list
                return jsonify({'idea_list': idea_list}), 200
        else:
            return jsonify({'message': 'No idea generated!'}), 400

    else:
        return jsonify({'message': 'Please specify question!'}), 400


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False, )