-- lists the number of records witht the same score
SELECT score COUNT(score) as 'number' FROM second_table GROUP BY score ORDER BY score ORDER BY number DESC;
