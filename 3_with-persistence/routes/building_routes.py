from services import building_service
from flask import request


def route(app):
    @app.route('/buildings', methods=['GET'])
    def get_buildings():
        buildings = building_service.get_all_buildings()
        return {
            'data': buildings
        }

    @app.route('/buildings/<id>', methods=['GET'])
    def get_building(id):
        return building_service.get_building(id)
        
    @app.route('/buildings/<building_id>/locations', methods=['GET'])
    def get_building_locations(building_id):
        return {
            'data': building_service.get_building_locations(building_id)
        }

    @app.route('/buildings', methods=['POST'])
    def create_building():
        building = request.json
        name = building['name']

        persisted = building_service.save(name)
        return persisted, 201