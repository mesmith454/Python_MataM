from flask import Flask
app = Flask(__name__) #flask constructor takes name of curren module (__name__) as argument

@app.route('/flask') #tells app which url should call assoc func
def hello_flask():
    return 'Hello Flask'

@app.route('/python/')
def hello_python():
    return 'Hello Python'
    app.run(debug = True) #runs application on local development server. parameters: host, port, debug, options. all optional