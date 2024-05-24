-- List all genres from 'hbtn_0d_tvshows' and display number of shows linked to each
-- Each record should display tv_genres.name, number of shows
-- Don't display a genre that doesn't have any shows linked
-- Results must be sorted descending order by number of shows linked
-- Can only use one SELECT statement
SELECT 
	g.name AS genre, 
	COUNT(t.genre_id) AS number_of_shows
FROM 
	tv_genres g
JOIN 
	tv_show_genres t ON g.id = t.genre_id
GROUP BY 
	g.name
HAVING 
	COUNT(t.genre_id) > 0
ORDER BY 
	number_of_shows DESC;
