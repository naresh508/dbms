Q1="SELECT COUNT(id) from Movie WHERE year=2002 AND name LIKE 'ha%' AND rank>2;"

Q2="SELECT MAX(rank) from Movie WHERE name LIKE 'Autom%' AND (year=1983 OR year=1994);"

Q3="SELECT COUNT(id) from Actor WHERE gender='M' AND (fname LIKE '%ei' OR lname LIKE 'ei%');"

Q4="SELECT AVG(rank) from movie WHERE (year=1993 OR year=1995 OR year=2000) AND rank>=4.2;"

Q5="SELECT SUM(rank) from movie WHERE name LIKE '%HAry%' AND (year BETWEEN 1981 AND 1984) AND rank<9;"

Q6="SELECT MIN(year) from Movie WHERE rank=5;"

Q7="SELECT COUNT(id) from ACTOR WHERE gender='F' AND fname==lname;"

Q8="SELECT DISTINCT fname from Actor WHERE lname LIKE '%ei' ORDER BY fname ASC LIMIT 100;"

Q9="SELECT id,name AS movie_title,year from Movie WHERE year IN(2001,2002,2005,2006) LIMIT 25 ;"

Q10="SELECT DISTINCT lname from Director WHERE fname IN('Yeud','Wolf','Vicky') ORDER BY lname ASC LIMIT 5;"