Q1=" SELECT COUNT(id) from MOVIE WHERE year<2000;"

Q2="SELECT AVG(rank) from MOVIE WHERE year=1991;"

Q3="SELECT MIN(rank) from MOVIE WHERE year=1991;"

Q4="SELECT fname,lname from ACTOR  INNER JOIN CAST ON pid==id WHERE mid=27;"

Q5="SELECT COUNT(mid) from ACTOR INNER JOIN CAST ON pid==id WHERE fname='Jon' AND lname='Dough';"

Q6="SELECT name from MOVIE WHERE name LIKE 'Young Latin Girls%' AND year BETWEEN 2003 AND 2006;"

Q7="SELECT DISTINCT fname,lname from DIRECTOR AS D INNER JOIN MOVIEDIRECTOR AS MD ON D.id==MD.did INNER JOIN MOVIE AS M ON M.id==MD.mid WHERE NAME LIKE 'Star Trek%';" 

Q8="SELECT name from MOVIE AS m INNER JOIN DIRECTOR AS d INNER JOIN MOVIEDIRECTOR AS md INNER JOIN ACTOR AS a INNER JOIN CAST AS c ON m.id==md.mid  AND d.id==md.did AND a.id==c.pid AND m.id==c.mid  WHERE (d.fname='Jackie (I)' AND d.lname='Chan') AND (a.fname='Jackie (I)' AND a.lname='Chan') ORDER BY NAME ASC;"

Q9="SELECT fname,lname from DIRECTOR AS D  INNER JOIN MOVIEDIRECTOR AS MD ON D.id==MD.did INNER JOIN MOVIE AS M ON M.id==MD.mid WHERE YEAR=2001 GROUP BY D.id HAVING COUNT(m.id)>=4 ORDER BY fname ASC,lname DESC;"

Q10="SELECT gender,COUNT(id) from ACTOR GROUP by gender HAVING gender='M' OR gender='F' ORDER BY gender A;"

Q11="SELECT a.name,b.name,a.rank,a.year from MOVIE AS a CROSS JOIN MOVIE AS b WHERE a.name!=b.name AND a.rank==b.rank AND a.year==b.year ORDER BY a.name ASC LIMIT 100"

Q12="SELECT a.fname,m.year,m.rank from ACTOR AS a INNER JOIN CAST AS c INNER JOIN MOVIE AS m ON a.id==c.pid AND m.id=c.mid ORDER BY a.fname ASC,m.year DESC LIMIT 100;"

Q13="SELECT a.fname,d.fname,AVG(m.rank) FROM ACTOR a INNER JOIN CAST AS c INNER JOIN MOVIE AS m INNER JOIN DIRECTOR AS d INNER JOIN MOVIEDIRECTOR AS md ON a.id==c.pid AND m.id==c.mid AND d.id==md.did AND m.id==md.mid GROUP BY md.did,a.id HAVING COUNT(m.id)>=5 ORDER BY avg(m.rank) DESC,d.fname ASC,a.fname DESC LIMIT 100;"