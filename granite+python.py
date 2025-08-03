import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_roadmap', methods=['GET'])
def get_roadmap():
    response = {
        "generic": [ ... ]  # The above JSON inside here
    }
    return jsonify(response)
