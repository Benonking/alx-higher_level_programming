-- list all shows contsained in db
--- display tv_show.title, tv_show_genres.genre_id
-- if a show doesnt have a genre display null
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
