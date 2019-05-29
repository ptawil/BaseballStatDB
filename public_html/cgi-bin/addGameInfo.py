#!/usr/bin/python3                                                           
                                                                             
import mysql.connector, cgi
print("Content-type:text/html\r\n\r\n")
cnx = mysql.connector.connect(user='ptawil', password='ptawil', database='ptawil', host='localhost')

cursor = cnx.cursor()

form = cgi.FieldStorage()
submit = form.getvalue("submitted")
if submit:
    homeTeam = form.getvalue("home_team").split(":")[0]
    #homeScore = form.getvalue("home_score")
    awayTeam = form.getvalue("away_team").split(":")[0]
    date = form.getvalue("date")
    #awayScore = form.getvalue("away_score")
    query = "INSERT INTO game (game_date, home_team_id, away_team_id) VALUES (%s, %s, %s)"
    vals = (date, homeTeam, awayTeam)
    cursor.execute(query, vals)
    cnx.commit()
    query = "SELECT LAST_INSERT_ID()"
    cursor.execute(query)
    gameId = cursor.fetchone()[0]
    print('<html>')
    print('<head>')
    print('<title>Add Game Info</title>')
    print('</head>')
    print('<body>')
    print('<form action="addPlayerStats.py">')
    query = "SELECT player_id, name, position FROM player, team WHERE player.team_id = team.team_id AND team.team_id = %s"
    val = (homeTeam,)
    cursor.execute(query, val)
    print('<table> <caption> HOME TEAM PLAYERS </caption> <tr> <th> Played? </th> <th> Player ID/ Player Name/Position </th> <th> Number of Runs </th> <th> Number of At Bats </th> <th> Number of Hits </th> <th> Number of Home Runs </th> </tr>')
    count = 1
    for row in cursor:
        print('<tr>')
        print('<td> <input type="checkbox" name="player' + str(count)+ '"> </td>')
        print('<td> <input type="text" name="playerInfo' + str(count)+'" value="'+ str(row[0]) + " " + row[1] + " " + row[2] + '" readonly></td>')
        print('<td> <input type="number" name="runs'+str(count)+'"> </td>')
        print('<td> <input type="number" name="num_of_abs' + str(count) +'"> </td>')
        print('<td> <input type="number" name="num_of_hits'+str(count)+'"> </td>')
        print('<td> <input type="number" name="homeruns' + str(count)+'"> </td>')
        print('</tr>')
        count+=1
    val = (awayTeam,)
    cursor.execute(query, val)
    print('</table>')
    print('<table> <caption> AWAY TEAM PLAYERS </caption> <tr> <th> Played? </th> <th> Player ID/ Player Name/Position </th> <th> Number of Runs </th> <th> Number of At Bats </th> <th> Number of Hits </th> <th> Number of Home Runs </th> </tr>')
    for row in cursor:
        print('<tr>')
        print('<td> <input type="checkbox" name="player' + str(count) +'"> </td>')
        print('<td> <input type="text" name="playerInfo' + str(count) +'" value="' + str(row[0]) + " " + row[1] + " " + row[2] + '" readonly></td>')
        print('<td> <input type="number" name="runs' + str(count) +'"> </td>')
        print('<td> <input type="number" name="num_of_abs' + str(count)+'"> </td>')
        print('<td> <input type="number" name="num_of_hits' + str(count) +'"> </td>')
        print('<td> <input type="number" name="homeruns' + str(count) + '"> </td>')
        print('</tr>')
        count+=1
    print('</table> <br>')
    print('<input type="hidden" name="numOfPlayers" value="' + str(count-1) +'">')
    print('<input type="hidden" name="game_id" value="' + str(gameId) +'">')
    print('<input type="submit" value="Submit">')
    print('</form>')
    print('</body>')
    print('</html>')
    


print('<html>')
print('<head>')
print('<title>Add Game Info</title>')
print('</head>')
print('<body>')
print('<form action="addGameInfo.py">')
print('Home Team:  <select name="home_team">')
query="SELECT team_id,team_name from team"
cursor.execute(query)
for row in cursor:
    print('<option> ' + str(row[0]) + ':' + row[1] + '</option>')
print('</select> <br>')
print('Away Team:  <select name="away_team">')
query="SELECT team_id,team_name from team"
cursor.execute(query)
for row in cursor:
    print('<option> ' + str(row[0]) + ':' + row[1] + '</option>')
print('</select> <br>')
print('<input type="date" name="date"> <br>')
print('<input type="submit" name="submitted" value="Submit">')
print('</form>')
print('</body>')
print('</html>')       
cursor.close()
cnx.close()
