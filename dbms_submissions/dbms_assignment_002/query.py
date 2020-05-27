Q1="SELECT * from Movie ORDER BY rank DESC LIMIT 10;"

Q2="SELECT * from Movie ORDER BY rank DESC LIMIT 10 OFFSET 10;"

Q3="SELECT name from Movie WHERE year>2004;"

Q4="SELECT name from Movie WHERE rank<1.1;"

Q5="SELECT * from Movie WHERE year BETWEEN 2004 AND 2006;"

Q6="SELECT name,year from Movie WHERE name LIKE 'Harry%';"

Q7="SELECT * from Actor WHERE fname='Christin' AND lname!='Watson';"

Q8="SELECT * from Actor WHERE fname='Woody' AND lname='Watson';"

Q9="SELECT name from Movie WHERE year=1990 AND rank=5;"

Q10="SELECT * from Actor WHERE fname='Christin' AND lname='Watson';"

Q11="SELECT name from Movie WHERE year BETWEEN 2003 AND 2005;"

Q12="SELECT DISTINCT year from Movie ORDER BY year ASC;"

Q13="""SELECT * from Actor WHERE (fname='Christin' OR lname='Watson') AND gender='M' ORDER BY fname ASC LIMIT 10;"""