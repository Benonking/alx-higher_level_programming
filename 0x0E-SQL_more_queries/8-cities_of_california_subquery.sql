-- list all cities that can be found in the db
SELECT id, name 
FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = "califonia") GROUP BY id ASC; 
