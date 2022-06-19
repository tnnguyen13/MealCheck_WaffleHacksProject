from http import HTTPStatus
from flask import Flask, jsonify, request

app = Flask(__name__)

todos = {}


@app.get("/todos")
def list():
    return jsonify(list(todos.values()))

@app.post("/todos")
def create():
    summary = request.json.get("summary")
    description = request.json.get("descriptions")
    if summary is None:
        return jsonify(message= "invalid request"), HTTPStatus.BAD_REQUEST
    id = randint(0, 100000)
    todos[id] = {"id": id, "summary": summary, "description": description, "complete" : False}
    return jsonify(todos[id])

@app.get("/todos/<int:id>")
def read(id):
    pass