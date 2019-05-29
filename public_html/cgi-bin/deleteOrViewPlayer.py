#!/usr/bin/python3

import mysql.connector, cgi
print("Content-type:text/html\r\n\r\n")
cnx = mysql.connector.connect(user='ptawil', password='ptawil', database='ptawil', host='localhost')

cursor = cnx.cursor()

form = cgi.FieldStorage()
submit = form.getvalue("submitted")
if submit:
    team = form.getvalue("team")
    teamId = form.getvalue("team").split(":")[0]
    query = "SELECT player_id, name, position, battingAverage(player_id), homeruns(player_id) FROM player JOIN team ON player.team_id = team.team_id WHERE team.team_id = %s"
    val = (teamId,)
    cursor.execute(query, val)
    players = cursor.fetchall()
    query = "SELECT team_id, team_name FROM team"
    cursor.execute(query)
    teams = cursor.fetchall()
    dropdown = '<select name="team">'
    for row in teams:
        if str(row[0]) == teamId:
            dropdown+='<option selected> ' + str(row[0]) + ':' + row[1] + '</option>'
        else:
            dropdown+='<option>' + str(row[0]) + ":" + row[1] + '</option>'
    dropdown+='</select>'
    print('<html>')
    print('<head>')
    print('<title>View/Delete Players By Team</title>')
    print('</head>')
    print('<body>')
    print('<table>')
    print('<tr> <th> Player Id </th> <th> Name </th> <th> Position </th> <th> Batting Average </th> <th> Home Runs </th> <th> Team </th> <th> Link to Delete </th> <th> Update Player Info </th> </tr>')
    for row in players:
        print('<form action="updatePlayerInfo.py">')
        print('<tr>')
        print('<td> <input type="text" size="6" name="player_id" value="' + str(row[0]) + '" readonly></td>')
        print('<td> <input type="text" name="name" value="' + row[1] + '"> </td>')
        print('<td> <input type="text" size="5" name="position" value="' + row[2] + '"></td>')
        print('<td> <input type="text" size="7" value="' + str(row[3]) + '" readonly></td>')
        print('<td> <input type="text" size="5" value="'+str(row[4]) + '" readonly></td>')
        print('<td> '+ dropdown + '</td>')
        print('<td> <a href="deletePlayer.py?playerId=' + str(row[0]) +'&team=' + team + '"> Delete Player </a> </td>')
        print('<td> <input type="submit" value="Update"> </td>')
        print('</tr>')
        print('</form>')
    print('</table>')
    print('</body>')
    print('</html>')
    
print('<html>')
print('<head>')
print('<title>View/Delete/Update Players By Team</title>')
print('</head>')
print('<body>')
print('<form action="deleteOrViewPlayer.py">')
print('<select name="team">')
query="SELECT team_id,team_name from team"
cursor.execute(query)
for row in cursor:
    print('<option> ' + str(row[0]) + ':' + row[1] + '</option>')
print('</select>')
print('<input type="submit" name="submitted" value="Submit">')
print('</form>')
print('<a href="../baseball.html"> Back to home page </a>')
print('</body>')
print('</html>')
cursor.close()
cnx.close()
