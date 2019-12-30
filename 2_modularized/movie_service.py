# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 09:30:16 2019

The movie_service will mimic a persistence
layer by storing movies in a list.

@author: Mitch
"""
from flask_api import exceptions

movies = []

def save_movie(movie):
    movie.id = len(movies) + 1
    movie_dict = movie.__dict__
    movies.append(movie_dict)
    return movie_dict

def get_movie(id):
    id = id - 1
    if id >= len(movies):
        raise exceptions.NotFound('No movie with id %d' % id)
    return movies[id]

def get_movies():
    return movies