-- list a;ll cities cotained in the db
-- display cities.id, cities.name states.name
-- asc by cites.id
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
