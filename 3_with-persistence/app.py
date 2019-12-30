from flask import Flask 
from flask_api.exceptions import NotFound

from routes import location_routes
from routes import building_routes

app = Flask(__name__)

# Pass app object off to functions which define
# routing for specific domains
location_routes.route(app)
building_routes.route(app)

# Define error handlers
@app.errorhandler(NotFound)
def handle_not_found(e):
    return {}, 404

# Start app
if __name__ == '__main__':
    app.run()
