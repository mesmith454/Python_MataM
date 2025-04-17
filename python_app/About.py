from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def default():
    return 'This is my first Flask App'

@app.route('/about')
def about():
    return 'Megan Mata, 33F, Network Administration Certification Track.'

@app.route('/fortune',methods = ['GET', 'POST'])
def fortune_form():
    if request.method == 'POST':
        return render_template('fortune.html')
        
    else:
        #retrieve the form data
        user = request.form['user']
        color = request.form['color']
        number = request.form['number']

        return render_template('result.html', user=user, color=color, number=number)


    


if __name__ == '__main__':
    app.run(debug = True)
