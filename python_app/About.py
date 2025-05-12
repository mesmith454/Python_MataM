from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.sqlite3'
# needed for post function DON'T TAKE IT OUT AGAIN.
app.config['SECRET_KEY'] = "random string"

movies = [
    {"title": "Titanic",
     "year": "1997"},
    {"title": "O Brother Where Art Thou",
     "year": "2000"}
]

db = SQLAlchemy(app)
class Game(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    dev = db.Column(db.String(50))
    genre = db.Column(db.String(200))
    rel = db.Column(db.String(10))
    summ = db.Column(db.String(80))

    def __init__(self, name, dev, genre, rel, summ):
        self.name = name
        self.dev = dev
        self.genre = genre
        self.rel = rel
        self.summ = summ


@app.route('/')
def default():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

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
    return render_template('show_all.html', games = Game.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        #error checking to ensure all fields filled 
        if not request.form['name'] or not request.form['dev'] or not request.form['genre'] or not request.form['rel'] or not request.form['summ']:
            flash('Please enter all fields', 'error')
        #pull data from form       
        else:
            game = Game(request.form['name'], request.form['dev'], request.form['genre'], request.form['rel'], request.form['summ'])
            #submit form data as a game object and show success message
            db.session.add(game)
            db.session.commit()
            flash('Game successfully added!')
            return redirect(url_for('show_all'))
    return render_template('new.html')

@app.route('/game/<int:gid>/')
def game(gid):
    this_game = Game.query.get(gid)
    return render_template('game.html', game = this_game)

# endpoint: get list of movies (GET)
@app.route('/movies')
def get_movies():
    return jsonify(movies)

# endpoint: post new movie to list (POST)
@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        movie = request.form
        response_data = {"message": "Succesful Submit", "movie": dict(movie)}
        movies.append(movie)
        return jsonify(response_data), 201
    return render_template('add_movie.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True, host="0.0.0.0", port=5000)