from flask import Flask, jsonify,request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": True },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():

    list_todos = jsonify(todos)

    return list_todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    todos.append(request.json)

    print("Incoming request with the following body", todos)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):

    todos.pop(position)

    print("This is the position to delete:", position)
    
    return todos

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
