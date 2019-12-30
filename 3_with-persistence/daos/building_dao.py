from flask_api import exceptions

from daos import db

def get_all_buildings():
    curs = db.get_cursor()
    curs.execute('SELECT id, name FROM buildings')
    return db.map_list(curs.fetchall())

def get_building(id):
    curs = db.get_cursor()
    curs.execute('SELECT id, name FROM buildings WHERE id = %s', (id))
    
    if curs.rowcount < 1:
        raise exceptions.NotFound()

    return curs.fetchone().copy()

def save(building_name):
    curs = db.get_cursor()
    curs.execute('INSERT INTO buildings (name) VALUES (%s) RETURNING id, name', (building_name,))
    db.commit()
    return curs.fetchone().copy()