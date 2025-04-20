from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/')
def default():
    return 'Welcome to my first flask app'

@app.route('/about')
def about():
    return 'Megan Mata, 33F, Network Administration Certification Track.'

@app.route('/fortune',methods = ['GET', 'POST'])
def fortune():
    # when a post method is performed
    if request.method == "POST":
        #grab form input for name
        name = request.form.get("user")
        # grab form input for color
        color = request.form.get("color")
        # grab form input for number
        number = request.form.get("number")
        return name +", you have " + number +" "+ color + " objects in your future."
    return render_template('fortune.html')



if __name__ == '__main__':
    app.run(debug = True)
