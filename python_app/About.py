from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def default():
    return 'This is my first Flask App'

@app.route('/about')
def about():
    return 'Megan Mata, 33F, Network Administration Certification Track.'

@app.route('/fortune',methods = ['POST'])
def fortune_form():
    return render_template('fortune.html')

def accept_input():
    return 'Input Accepted'

def return_fortune():
    return 'Here is your fortune:'
    


if __name__ == '__main__':
    app.run(debug = True)
