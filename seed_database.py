"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb ratings")
os.system("createdb ratings")

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())


movies_in_db = []
for movie in movie_data:
    overview = movie['overview']
    poster_path = movie['poster_path']
    title = movie['title']
    release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')
    
    movies_in_db.append(crud.create_movie(title, overview, release_date, poster_path))

# Specify the file where the function or methods come from (ex: crud, model...)
model.db.session.add_all(movies_in_db)
model.db.session.commit()


for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    user = crud.create_user(email, password)
    model.db.session.add(user)
    
    list_ratings = []
    for i in range(10):
        rating = crud.create_rating(user, choice(movies_in_db), randint(1,5))
        list_ratings.append(rating)

    model.db.session.add_all(list_ratings)

model.db.session.commit()


# [{'overview': 'The near future, [...] search of the unknown.',
#   'poster_path': 'https://image.tmdb.org/t/p/original//xBHvZcjRiWyobQ9kxBhO6B2dtRI.jpg',
#   'release_date': '2019-09-20',
#   'title': 'Ad Astra'}
#   ...
#   ]    