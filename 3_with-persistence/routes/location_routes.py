from flask import request
from services import location_service as ls

def route(app):
    @app.route('/locations', methods=['GET'])
    def get_locations():
        return {
            'data': ls.get_all_locations()
        }

    @app.route('/locations/<id>', methods=['GET'])
    def get_location(id):
        return ls.get_location(id)

    @app.route('/locations', methods=['POST'])
    def create_location():
        location_dict = request.json
        building_id = location_dict['building_id']
        number = location_dict['number']

        return ls.save(building_id, number), 201