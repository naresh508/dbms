Q1='''select p.player_id,p.team_id,p.jersey_no,p.name,p.date_of_birth,
      p.age from player p inner join matchcaptain mc on  
      p.player_id=mc.captain left join goaldetails gd on 
      gd.player_id=p.player_id and p.team_id=mc.team_id where 
      gd.goal_id is null;
'''

Q2='''select team_id,count(match_no) as no_of_games from matchteamdetails 
      group by team_id;'''

Q3='''SELECT t.team_id,((select count(goal_id) from goaldetails gd where 
      gd.team_id=t.team_id group by gd.team_id)*1.0)/(select count
      (p.player_id) from player p where p.team_id=t.team_id group by 
      p.team_id) as avg_goal_score from team t group by team_id having 
      avg_goal_score is not null;'''  


Q4='''select captain,count(captain) as no_of_times_captain from matchcaptain group by captain;'''

#Q5='''select count(mc.captain) from matchcaptain mc inner join match m on p.player_id=mc.captain mc.match_no=m.match_no and m.player_of_match=mc.captain group by captain;'''
Q5="SELECT COUNT(captain) from (select mc.captain from matchcaptain mc inner join match m on mc.match_no=m.match_no where m.player_of_match=mc.captain group by captain);"

Q6='''SELECT DISTINCT mc.captain from MATCHCAPTAIN mc where NOT EXISTS(select m.player_of_match from 
    match m inner join player p on m.player_of_match=p.player_id AND mc.captain=p.player_id);'''

Q7="select strftime('%m',m.play_date) AS month,count(m.match_no) from match m group by month"


Q8="select p.jersey_no,count(mc.captain) as no_captains from matchcaptain mc inner join player p on p.player_id=mc.captain group by p.jersey_no order by count(mc.captain) DESC,p.jersey_no DESC"

Q9="select p.player_id,(select avg(m.audience) from match m inner join matchteamdetails md on  m.match_no=md.match_no and md.team_id=p.team_id) as avg_audience from player p group by p.player_id order by avg_audience desc,p.player_id desc;"

Q10="select t.team_id,avg(p.age) from player as p inner join team t on p.team_id=t.team_id group by t.team_id"

Q11="select avg(age) as avg_age_of_captain  from player p inner join matchcaptain mc on p.player_id=mc.captain;"
      
Q12="select strftime('%m',date_of_birth) as month,count(player_id) no_of_players from player group by month order by count(player_id) DESC,month desc"


Q13="""SELECT mc.captain,count(md.match_no) as no_of_wins
       from matchteamdetails md  inner join
       matchcaptain as mc on md.team_id=mc.team_id and 
       mc.match_no=md.match_no where md.win_lose='W' group by mc.captain
       order by no_of_wins desc;"""

      