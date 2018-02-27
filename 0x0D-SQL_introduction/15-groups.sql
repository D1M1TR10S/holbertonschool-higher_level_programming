-- List number of instances of score in second_table of current db
SELECT score,
COUNT(score) AS "number"
FROM second_table
GROUP BY score DESC;
