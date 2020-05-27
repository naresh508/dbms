Q1='''SELECT a.id,a.fname,a.lname,a.gender from ACTOR a inner join cast as c
      inner join movie m on a.id=c.pid and m.id=c.mid where m.name like 
      "Annie%" '''
      

Q2='''SELECT m.id,m.name,m.rank,m.year from movie m inner join moviedirector md 
     inner join director d on m.id=md.mid and d.id=md.did where 
     (d.fname="Biff" and d.lname="Malibu") and m.year IN(1999,1994,2003) 
      order by m.rank DESC,m.year ASC;''' 
      
Q3='''SELECT m.year,count(m.id) as no_of_movies from movie m group by 
      m.year having avg(m.rank)>(select avg(rank) from movie)'''


Q4='''select m.id,m.name,m.year,m.rank from movie m where m.year=2001 
      and m.rank<(select avg(rank) from movie where year=2001) order by 
      m.rank desc limit 10'''


Q5='''select m.id,(select count(a.gender) from actor a inner join cast c 
      on a.id=c.pid and c.mid=m.id where a.gender="F" group by c.mid) 
      no_of_female_actors,(select count(a.gender) from actor a inner join 
      cast c on a.id=c.pid and c.mid=m.id where a.gender=="M" group  by c.mid) 
      no_of_male_actors from movie m order by m.id ASC limit 100;'''


Q6='''select distinct c.pid from cast c inner join actor a inner join movie m
     on c.pid=a.id and c.mid=m.id group by m.id,c.pid having 
     count(distinct c.role)>1 order by c.pid ASC limit 100'''


Q7='''select d.fname,count(d.fname) from director d group by d.fname 
     having count(d.fname)>1'''
      

Q8='''select d.id,d.fname,d.lname from director d where exists
      (select md.did from moviedirector md inner join cast c on d.id=md.did 
      and c.mid=md.mid group by c.mid having count(c.pid)>=100) and not 
      exists(select md.did from moviedirector md inner join cast c on 
      d.id=md.did and c.mid=md.mid group by c.mid having count(c.pid)<100);'''       
      