-- list all shows in db withoud a genre link
SELECT tv_shows.title, tv_show_genre.genre_id
FROM tv_shows
LEFT JOIN tv_shows_genres
ON tv_shows.id = tv_show_genre_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genre.genre_id ASC;














