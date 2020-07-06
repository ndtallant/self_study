'''Basic flask app.'''

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/api')
def api():
    return jsonify({'hello': 'api'})

