import json

from flask import Flask, request, jsonify

from tasks import get_task_class

app = Flask(__name__)

@app.route("/integrations/demo/", methods=['POST'])
def router():
    cls = get_task_class(request.json)
    return jsonify(cls().call(request.json))

