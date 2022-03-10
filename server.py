"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!
@app.route('/')
def show_homepage():
    """ Show homepage """

    return render_template('homepage.html')


@app.route('/movies')
def show_movies():
    """ Show all movies """

    movies = crud.show_all_movies()

    return render_template("all_movies.html", movies=movies)


@app.route('/movies/<movie_id>')
def show_movie_details(movie_id):
    """ Show details about a movie """

    movie = crud.get_movie_by_id(movie_id)

    return render_template("movie_details.html", movie=movie)


@app.route('/users')
def show_users():
    """ Show all users """

    users = crud.show_all_users()

    return render_template("users.html", users = users)


@app.route('/users/<user_id>')
def show_user_detail(user_id):
    """ Show details about a user """

    user = crud.user_by_id(user_id)

    return render_template("user_details.html", user=user)


@app.route('/new_users', methods = ['POST'])
def register_user():
    """ Create a new user """

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user:
        flash('This email has already been used. Try a different email.')
    else:
        new_user = crud.create_user(email, password)
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been successfully created. You can log in now')

    return redirect('/')


@app.route('/login', methods = ['POST'])
def login():
    """ Login with email and password """

    email = request.form.get('email')
    password = request.form.get('password')

    user_password = crud.get_password_by_email(email)

    if user_password == password:
        session['user'] = crud.get_user_id_by_email(email)
        flash('Logged in!')
    else:
        flash('Incorrect password, please try again!')

    return redirect('/')


@app.route('/rate_movie', methods = ['POST'])
def rate_a_movie():
    """ Rate a movie """

    movie_name = request.form.get('movie_name')
    score = request.form.get('score')
    user = crud.user_by_id(session['user'])

    movie = crud.get_movie_by_name(movie_name)

    if movie:
        new_rating = crud.create_rating(user, movie, score)
        db.session.add(new_rating)
        db.session.commit()
        flash('You successfully rated a movie!')
    else:
        flash('Sorry this movie is not in our list. Please choose a different movie to rate')

    return redirect ('/')



if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
