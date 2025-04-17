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
    if request.method == 'POST':
        return render_template('fortune.html') #render base template-should be first page loaded
    else:
        return 'fortune goes here' #currently loading first
    #take user input
    #return user fortune

if __name__ == '__main__':
    app.run(debug = True)
