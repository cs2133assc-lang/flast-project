import os
from flask import Flask, jsonify
import json

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/api')
def get_data():
    file_path = os.path.join(BASE_DIR, 'data.json')
    with open(file_path, 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
