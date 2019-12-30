# API Description

## Models
1. Building - Some building for which we are tracking locations. Has ownership of related Locations.
  * id - int
  * name - string
2. Location - Some location within or associated to a building.
  * id - int
  * number - string
  * building_id - int

## API
### Building
1. GET - /buildings
2. GET - /buildings/<id>
3. GET - /buildings/<id>/locations
4. POST - /buildings

### Location
1. GET - /locations
2. GET - /locations/<id>
3. POST - /locations