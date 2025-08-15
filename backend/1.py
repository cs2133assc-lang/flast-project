import os
from flask import Flask, request, jsonify
import json

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TODO_FILE = os.path.join(BASE_DIR, 'todo.json')

# Ensure the file exists
if not os.path.exists(TODO_FILE):
    with open(TODO_FILE, 'w') as f:
        json.dump([], f)

@app.route('/api', methods=['GET'])
def get_data():
    with open(TODO_FILE, 'r') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    data = request.get_json()

    item_name = data.get('itemName')
    item_description = data.get('itemDescription')

    if not item_name or not item_description:
        return jsonify({"error": "Both itemName and itemDescription are required"}), 400

    # Load existing todos
    with open(TODO_FILE, 'r') as f:
        todos = json.load(f)

    # Append new todo
    new_todo = {
        "itemName": item_name,
        "itemDescription": item_description
    }
    todos.append(new_todo)

    # Save updated list
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

    return jsonify({"message": "Todo item added successfully", "todo": new_todo}), 201

if __name__ == '__main__':
    app.run(debug=True)
