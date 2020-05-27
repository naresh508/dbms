Q1="SELECT fname,lname from ACTOR INNER JOIN CAST ON id==pid WHERE mid=12148;"

Q2="SELECT COUNT(mid) from ACTOR INNER JOIN CAST ON id==pid WHERE fname='Harrison (I)' AND lname='Ford';"

Q3="SELECT DISTINCT(pid) from MOVIE INNER JOIN CAST ON id==mid WHERE name LIKE 'Young Latin Girls%';"

Q4="SELECT DISTINCT(actor_id) from MOVIE INNER JOIN CAST ON id==mid WHERE year BETWEEN 1990 AND 2000;"