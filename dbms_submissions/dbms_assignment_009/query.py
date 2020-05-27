Q1='''select AVG(age) from player'''

Q2='''SELECT match_no,play_date from match WHERE audience>50000 
      order by match_no ASC;'''

Q3='''SELECT team_id,count(win_lose) from matchteamdetails 
      where win_lose='W' group by team_id order by count(win_lose) 
      DESC,team_id ASC;'''
    
Q4='''select match_no,play_date from match WHERE stop1_sec>(
      select avg(stop1_sec) from match) order by match_no DESC'''    
    
Q5='''select m.match_no,t.name,p.name from match as m inner join team as t 
      inner join matchcaptain as mc inner join player AS p on  
      m.match_no=mc.match_no AND t.team_id=mc.team_id 
      and p.player_id=mc.captain order by m.match_no ASC,t.name ASC'''


Q6='''select m.match_no,p.name,p.jersey_no from match as m INNER JOIN 
      player as pon m.player_of_match=p.player_id group by m.match_no 
      order by match_no ASC'''
   
Q7='''select t.name,avg(age) from player inner join team as t on 
      player.team_id=t.team_id group by t.team_id having avg(age)>26 
      order by t.name ASC'''  


Q8='''select p.name,p.jersey_no,p.age,count(goal_id) from 
      goaldetails as gd inner join player as p on gd.player_id=p.player_id  
      where p.age<=27 group by p.player_id order by count(goal_id) 
      DESC,p.name ASC'''
    
    
Q9='''select gs.team_id,((select count(goal_id) from goaldetails  gd 
      WHERE gd.team_id=gs.team_id group by gd.team_id having 
      count(goal_id)>=1 ) * 100.0)/(select count(goal_id) from 
      goaldetails gd) from goaldetails gs group by gs.team_id;'''                  

Q10='''select avg(gc) from (select count(goal_id) as gc from 
       goaldetails group by team_id)'''  

Q11='''SELECT p.player_id,p.name,p.date_of_birth from player as p 
       WHERE NOT EXISTS(select goal_id from goaldetails as gd 
       INNER JOIN MATCH AS m on gd.match_no=m.match_no  where 
       gd.match_no=m.match_no and gd.player_id=p.player_id group by 
       player_id having count(goal_id)!=0) order by p.player_id ASC;'''    
    
Q12='''select t.name,m.match_no,m.audience,m.audience-(select avg(audience) 
       from match as m inner join matchteamdetails as md on 
       m.match_no=md.match_no and t.team_id=md.team_id group by md.team_id) 
       from team as t inner join match as m inner join matchteamdetails as 
       md on t.team_id=md.team_id and m.match_no=md.match_no order by 
       m.match_no ASC;'''    