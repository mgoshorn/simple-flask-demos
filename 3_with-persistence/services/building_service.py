from daos import building_dao
from services import location_service

def get_all_buildings():
    return building_dao.get_all_buildings()

def get_building(id):
    return building_dao.get_building(id)

def get_building_locations(building_id):
    return location_service.get_locations_by_building(building_id)

def save(building_name):
    return building_dao.save(building_name)