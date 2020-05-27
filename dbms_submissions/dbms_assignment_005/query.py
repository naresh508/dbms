Q1="SELECT pid AS actor_id,COUNT(mid) AS no_of_movies from Cast GROUP BY pid;"

Q2="SELECT year,COUNT(id) from Movie GROUP BY year ORDER BY year ASC;"

Q3="SELECT year,AVG(rank) AS avg_rank from Movie GROUP BY year HAVING COUNT(year)>=10 ORDER BY year DESC;"

Q4="SELECT year,MAX(rank) AS max_rank from MOVIE GROUP BY year ORDER by year ASC;"

Q5="SELECT rank,COUNT(id) AS no_of_movies from Movie WHERE name LIKE 'a' GROUP BY rank;"