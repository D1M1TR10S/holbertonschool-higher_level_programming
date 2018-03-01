-- Lists all the cities in database hbtn_0d_usa
-- Joins cities and states to list state names

SELECT cities.id, cities.name, states.name
FROM cities LEFT JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
