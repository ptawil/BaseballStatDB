#!/usr/bin/python3

import mysql.connector, cgi
print("Content-type:text/html\r\n\r\n")
cnx = mysql.connector.connect(user='ptawil', password='ptawil', database='ptawil', host='localhost')

cursor = cnx.cursor()

form = cgi.FieldStorage()
submit = form.getvalue("submitted")
if submit:
    playerName = form.getvalue("playerName")
    position = form.getvalue("position")
    teamId = form.getvalue("team").split(":")[0]
    if form.getvalue("action") == "add": 
        query = "INSERT INTO player (name, position, team_id) VALUES (%s, %s, %s)"
        val = (playerName, position, teamId)
        cursor.execute(query, val)
        cnx.commit()
        print('<html>')
        print('<head>')
        print('<title>Add a player</title>')
        print('</head>')
        print('<body>')
        print('<p> Player Added </p>')
        print('</body>')
        print('</html>')
    else:
        query = "UPDATE player SET position = %s, team_id = %s WHERE name = %s"
        val = (position, teamId, playerName)
        cursor.execute(query, val)
        cnx.commit()
        print('<html>')
        print('<head>')
        print('<title>Update a player</title>')
        print('</head>')
        print('<body>')
        print('<p> Player updated </p>')
        print('</body>')
        print('</html>')
    
print('<html>')
print('<head>')
print('<title>Add/Update a Player</title>')
print('</head>')
print('<body>')
print('<form action="addOrUpdatePlayer.py">')
print('<input type="radio" name="action" value="add">Add player <br>')
print('<input type="radio" name="action" value="update">Update Player Info <br>')
print('Player Name: <input type="text" name="playerName"> <br>')
print('Position: <input type="text" name="position"> <br>')
print('Team: <select name="team">')
query="SELECT team_id,team_name from team"
cursor.execute(query)
for row in cursor:
    print('<option> ' + str(row[0]) + ':' + row[1] + '</option>')
print('</select>')
print('<input type="submit" name="submitted" value="Submit">')
print('</form>')
print('</body>')
print('</html>')
