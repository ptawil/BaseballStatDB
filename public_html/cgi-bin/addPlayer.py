#!/usr/bin/python3

import mysql.connector, cgi
print("Content-type:text/html\r\n\r\n")
cnx = mysql.connector.connect(user='ptawil', password='ptawil', database='ptawil', host='localhost')

cursor = cnx.cursor()

form = cgi.FieldStorage()
submit = form.getvalue("submitted")
print('<html>')
print('<head>')
print('<title>Add a Player</title>')
print('</head>')
print('<body>')
if submit:
    playerName = form.getvalue("playerName")
    position = form.getvalue("position")
    teamId = form.getvalue("team").split(":")[0] 
    query = "INSERT INTO player (name, position, team_id) VALUES (%s, %s, %s)"
    val = (playerName, position, teamId)
    cursor.execute(query, val)
    cnx.commit()        
    print('<p> Player Added </p>')

    

print('<form action="addPlayer.py">')
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
print('<a href="../baseball.html"> Back to home page </a>')
print('</body>')
print('</html>')
cursor.close()
cnx.close()
