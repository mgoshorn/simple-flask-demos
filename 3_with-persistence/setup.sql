-- Setup script for database tables and connection role

-- Remove resources if they exist already
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS buildings;
DROP ROLE IF EXISTS py_robot;

-- Create role - consider changing password
CREATE ROLE py_robot LOGIN PASSWORD 'p4ssw0rd';

-- Assume role of py_robot so that it will have permissions on created resources
SET ROLE py_robot;

-- Create tables
CREATE TABLE IF NOT EXISTS buildings (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL
);

CREATE TABLE IF NOT EXISTS locations (
    id SERIAL PRIMARY KEY,
    number VARCHAR(20) NOT NULL,
    building_id INTEGER REFERENCES buildings(id)
);

-- Insert some starting values
insert into buildings (name) values ('NEC');
insert into locations (number, building_id) values ('200A', 1), ('200B', 1);