from flask import Flask, redirect, url_for, render_template, request, jsonify
import random

app = Flask(__name__)

fortunes = {
    "colors": {
        "red": ["RA", "RB"],
        "yellow": ["YA", "YB"],
        "blue": ["BA", "BB"],
        "green": ["GA", "GB"],
    },
    "numbers": {
        "1": ["1A", "1B"],
        "2": ["2A", "2B"],
        "3": ["3A", "3B"],
        "4": ["4A", "4B"],
    }
}

@app.route('/')
def default():
    return render_template('fortune.html')

@app.route('/about')
def about():
    return 'Megan Mata, 33F, Network Administration Certification Track.'

# @app.route('/get_fortune',methods = ['GET', 'POST'])

    
      


if __name__ == '__main__':
    app.run(debug = True)
