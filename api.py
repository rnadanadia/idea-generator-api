import os
import json

from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome Idea Generator!'})

@app.route('/idea', methods=['GET'])
def get_idea():
    return jsonify({'message': 'Idea Generator!'}),200 # @TODO: get body from json file


@app.route('/idea', methods=['POST'])
def create_idea():
    data = request.get_json()
    print(data)
    return jsonify({'message': 'Idea Generator!'}),200 # @TODO: get ideas from Generator


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)