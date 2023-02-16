--list all genres from db and displays the number of shows linkewd to each
-- display <TV show genre> <Number of shows linked to this genmre>
-- first colum genre
-- second column number_of_shows
-- dnt siplay any show without a link

SELECT tv_genres.name AS genre, COUNT(*) AS 'number_shows'
      FROM tv_genres
INNER JOIN tv_show_genres
        ON tv_genres.id = tv_show_genres.genre_id
  GROUP BY genre
  ORDER BY number_shows DESC;
