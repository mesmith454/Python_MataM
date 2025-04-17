from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def default():
    return 'This is my first Flask App'

@app.route('/about')
def about():
    return 'Megan Mata, 33F, Network Administration Certification Track.'

@app.route('/fortune',methods = ['POST', 'GET'])
def fortune():
    return render_template('fortune.html')

if __name__ == '__main__':
    app.run(debug = True)