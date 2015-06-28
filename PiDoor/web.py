'''
Created on Jun 9, 2015

@author: simonsays
'''
from flask import Flask, request, jsonify
from PiDoor import action_handler

app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def index():
    data = request.get_json(force=True)
    action = data['action']
    args = data['args']
    response = action_handler.handle(action, args)
    return jsonify(code=200, response=response)

@app.errorhandler(Exception)
def all_exception_handler(error):
    return jsonify(code=500, error=str(error))
 
if __name__ == "__main__":
    action_handler.init()
    app.run(host='0.0.0.0', port=8888)
    action_handler.shutdown()