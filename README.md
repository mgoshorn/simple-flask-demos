# Sample Flask Apps
## What is Flask?
Flask is a microframework for building web applications and microservices applications.  Flask is lightweight but has convenient routing syntax that 
does a great job leveraging Python's introspection API to provide routing 
rules that would look familiar to anyone who has worked with Spring MVC,
in addition to Python's support for dictionary literals, which present themselves
similar to JavaScripts object literals (or JDK9+ map literal). As Flask can
directly convert dictionaries to JSON responses, it provides great flexibility
in building response payloads and simple routing.

## Dependencies
1. flask
2. flask-api

## Environment Setup
I recommend setting up environments to manage dependencies in Python. With 
Anaconda this can be accomplished by running: `conda create --name project-name`
to create an enviroment. You can switch to this environment using `conda activate project-name`.  Once the environment is created and activated you can install dependencies without affecting dependencies in other environments

## Dependency Installation
1. `conda install flask`
2. `pip install flask-api`
3. `conda install psycopg2`

Note: flask-api is used for some of the samples, but isn't available on conda, so it is installed with pip. Otherwise I would prefer to install directly through conda.

## Examples

1. bare-bones-server
This example contains a very simplistic, one-file script that will start a server
and expose a few endpoints to demonstrate simple functionality.

2. modularized
This project shows a more modularized application that separates logical functionality into several files, does some in-memory persistence, etc. It includes a model definition that demonstrates Python class syntax, although personally I would be more tempted to avoid this as Flask will not natively convert typical objects to JSON for convenient responses. You can easily convert an object to a dictionary for writing using `obj.__dict__`, however this can be very inconvenient if you have an array or objects that would all need to be converted. The downside of just using dictionaries is being stuck having to use brackets to access properties instead of the more traditional dot-syntax.

3. with-persistence
An example project which contains a more modularized project structure and database persistence. Considering running sql script to prepare database for usage.