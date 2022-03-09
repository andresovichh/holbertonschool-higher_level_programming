-- list cities in hbtn_0d_usa
-- asc by cities.id, 1 SELECT
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN  states ON cities.state_id = states.id;