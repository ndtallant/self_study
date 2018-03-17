from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True

@app.route('/')
@app.route('/<name>')
def index(name='Nick'):
    return 'Hello, {}'.format(name)
