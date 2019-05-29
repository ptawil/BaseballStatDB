#!/usr/bin/python3                                                                             
import mysql.connector, cgi
print("Content-type:text/html\r\n\r\n")
cnx = mysql.connector.connect(user='ptawil', password='ptawil', database='ptawil', host='localhost')
print('<html>')
print('<head>')
print('<title>View Game Info</title>')
print('</head>')
print('<body>')
cursor = cnx.cursor()
print('<h1> Click on a game to view </h1>')
query = "SELECT game.game_id, a.team_name, b.team_name, game.game_date, homeTeamScore(game.game_id), awayTeamScore(game.game_id)  FROM game JOIN team a ON game.home_team_id = a.team_id JOIN team b ON game.away_team_id = b.team_id" 
cursor.execute(query)
print('<table> <tr> <th> Game Date </th> <th> Home Team </th> <th> Away Team </th> <th> Link to View Game Stats</th> <th> Link to Delete Game </th> </tr>')
for (game_id, home_team, away_team, date, home_score, away_score) in cursor:
    print('<tr>')
    print('<td>' + str(date) + '</td>')
    print('<td>' + home_team + '-' + str(home_score) + '</td>')
    print('<td>' + away_team + '-' + str(away_score) + '</td>')
    print('<td> <a href="viewGameStats.py?game_id=' + str(game_id) + '"> View Game Stats </a> </td>')
    print('<td> <a href="deleteGame.py?game_id=' + str(game_id) + '"> Delete Game </a> </td>')
    print('</tr>')
print('</table>')
print('<a href="../baseball.html"> Home </a>')
print('</body>')
print('</html>')
cursor.close()
cnx.close()

    
