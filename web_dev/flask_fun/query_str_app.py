from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True

@app.route('/')
@app.route('/<name>')
def index(name='Nick'):
    return 'Hello, {}'.format(name)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    context = {'num1': num1, 'num2': num2}
    return render_template('add.html', **context)
