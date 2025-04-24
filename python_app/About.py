from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)
class games(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    dev = db.Column(db.String(50))
    genre = db.Column(db.String(200))
    rel = db.Column(db.String(10))
    detail = db.Column(db.String(80))

    def __init__(self, name, dev, genre, rel, summ):
        self.name = name
        self.dev = dev
        self.genre = genre
        self.rel = rel
        self.summ = summ

@app.route('/')
def default():
    return 'This is my first flask app'

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

@app.route('/show_all')
def show_all():
    # return the show_all template populated with info from database
    return render_template('show_all.html', games = games.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['dev'] or not request.form['genre'] or not request.form['rel'] or not request.form['summ']:
            flash('Please enter all fields', 'error')
        else:
            game = games(request.form['name'], request.form['dev'], request.form['genre'], request.form['rel'], request.form['summ'])

            db.session.add(game)
            db.session.commit()
            flash('Game successfully added!')
            return redirect(url_for('show_all'))
    return render_template('new.html')

@app.route('/summary')
def summary():
    return render_template('summary.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True)
