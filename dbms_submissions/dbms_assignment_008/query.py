Q1='''SELECT d.id,d.fname FROM director d WHERE EXISTS(
    SELECT m.id from MOVIE AS m INNER JOIN MOVIEDIRECTOR AS md on 
    m.id==md.mid WHERE d.id==md.did AND year>2000) AND NOT EXISTS (
    SELECT m.id from movie AS m INNER JOIN MOVIEDIRECTOR AS md on m.id==md.mid  
    where d.id==md.did  AND m.year<2000 )group by d.id;'''
    
Q2='''select  d.fname,(select m.name from MOVIE  AS m  
      INNER JOIN MOVIEDIRECTOR AS md ON m.id==md.mid WHERE md.did=d.id  
      order by rank DESC,m.name ASC LIMIT 1) AS name 
      from director AS d limit 100;'''    
      
Q3='''select * from  ACTOR AS a WHERE NOT EXISTS(
      select c.pid from cast as c INNER JOIN movie AS m on m.id=c.mid WHERE a.id=c.pid and m.year between 1990 AND 2000)order by a.id desc limit 100;'''      