-- Lists all rows with value in name of second_table in current DB
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
