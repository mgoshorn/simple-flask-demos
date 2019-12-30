from flask_api import exceptions

from daos import db

def get_locations_by_building(id):
    curs = db.get_cursor()
    curs.execute("""SELECT id, number, building_id 
        FROM locations WHERE building_id = %s""",
        (id,))
    
    return db.map_list(curs.fetchall())

def get_all_locations():
    curs = db.get_cursor()
    curs.execute('SELECT id, number, building_id FROM locations')
    return db.map_list(curs.fetchall())

def get_location(id):
    curs = db.get_cursor()
    curs.execute("""SELECT id, number, building_id 
        FROM locations WHERE id = %s""", (id,))
    
    if curs.rowcount < 1:
        raise exceptions.NotFound()

    return curs.fetchone().copy()

def save(building_id, number):
    curs = db.get_cursor()
    curs.execute("""INSERT INTO locations (building_id, number) 
        VALUES (%s, %s) RETURNING id, building_id, number""",
        (building_id, number))
    db.commit()
    return curs.fetchone().copy()