from daos import location_dao

def get_locations_by_building(building_id):
    return location_dao.get_locations_by_building(building_id)

def get_all_locations():
    return location_dao.get_all_locations()

def get_location(id):
    return location_dao.get_location(id)

def save(building_id, number):
    return location_dao.save(building_id, number)