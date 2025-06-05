from flask import Flask
app = Flask(__name__)
from flask import Flask, jsonify
from flask import request

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(dict(request_body))
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    global todos  # Paso 1: acceder a la lista global

    # Paso 2: verificar que la posición existe y eliminar la tarea
    if 0 <= position < len(todos):
        todos.pop(position)  # Método de Python para eliminar por índice
        return jsonify(todos)  # Paso 3: devolver la lista actualizada
    else:
        return jsonify({"error": "Posición no válida"}), 404

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)