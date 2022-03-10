""" CRUD operations"""

from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user


def show_all_users():
    """ Return a list of all users """

    users = User.query.all()

    return users


def user_by_id(user_id):
    """ Return a user by their id """

    user = User.query.get(user_id)

    return user


def get_user_by_email(email):
    """ Return a user by their email, if not existed, return None """

    user = User.query.filter(User.email==email).first()

    return user


def get_password_by_email(email):
    """ Return a password by user email """

    user = User.query.filter(User.email==email).first()
    
    return user.password

def get_user_id_by_email(email):
    """ Return user id by user email"""

    user = User.query.filter(User.email==email).first()

    return user.user_id

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie"""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    return movie


def show_all_movies():
    """Return a list of all movies"""

    movies = Movie.query.all()

    return movies


def get_movie_by_id(movie_id):
    """ Return a movie by its id """

    movie = Movie.query.get(movie_id)

    return movie


def get_movie_by_name(name):
    """ Return a movie by its name """

    movie = Movie.query.filter(Movie.title==name).first()

    return movie




def create_rating(user, movie, score):
    """ Create and return a rating"""

    rating = Rating(user=user, movie=movie, score=score)

    return rating
# 2 ways: create new user and movie, or get existing user and movie









if __name__ == '__main__':
    from server import app
    connect_to_db(app)