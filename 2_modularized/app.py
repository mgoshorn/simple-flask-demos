from flask import Flask
from flask import request
from flask_api import exceptions

from movie import Movie
from datetime import date
import movie_service
from flask_api.exceptions import NotFound

"""
More modularized app that tracks simple Movie data
See movie.py for understanding the structure of a movie.
Endpoints:
    GET:  /movies - list of movies
    GET:  /movies/<id> - movie by ID
    POST: /movies - create new resource given JSON data
"""

app = Flask(__name__)

@app.route('/movies', methods=['GET'])
def get_movies():
    payload = {
        'data': movie_service.get_movies()
    }
    return payload

@app.route('/movies/<id>', methods=['GET'])
def get_movie(id):
    if(id.isdigit()):
        exceptions.ParseError()
        
    return movie_service.get_movie(int(id))

@app.route('/movies', methods=['POST'])
def save_movie():
    data = request.json
    dt = date.fromisoformat(data['release_date'])
    movie = Movie(0, data['title'], dt)
    return movie_service.save_movie(movie), 201

@app.errorhandler(NotFound)
def handle_not_found(e):
    return {}, 404

if __name__ == '__main__':
    app.run()