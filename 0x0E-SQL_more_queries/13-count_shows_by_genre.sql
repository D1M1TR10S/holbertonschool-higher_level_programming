-- Lists all genres and how many shows are linked to each one

SELECT name AS "genres",
COUNT(tv_show_genres.genre_id) AS "number_shows"
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genres
ORDER BY number_shows DESC;
