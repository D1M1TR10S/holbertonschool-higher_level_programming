-- Lists all genres and how many shows are linked to each one

SELECT tv_genres.name,
COUNT(genre_id) AS "number_shows"
FROM tv_show_genres
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show_genres.show_id IS NOT NULL
GROUP BY tv_genres.name
ORDER BY number_shows DESC;
