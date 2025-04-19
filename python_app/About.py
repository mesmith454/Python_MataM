from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def default():
    return 'Welcome to my first flask app'

@app.route('/about')
def about():
    return 'Megan Mata, 33F, Network Administration Certification Track.'

@app.route('/fortune',methods = ['GET', 'POST'])
def get_fortune():
    return render_template('fortune.html')


if __name__ == '__main__':
    app.run(debug = True)
