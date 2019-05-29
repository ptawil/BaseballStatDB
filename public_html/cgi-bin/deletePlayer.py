#!/usr/bin/python3

import mysql.connector, cgi
print("Content-type:text/html\r\n\r\n")
cnx = mysql.connector.connect(user='ptawil', password='ptawil', database='ptawil', host='localhost')

cursor = cnx.cursor()

form = cgi.FieldStorage()
playerId = form.getvalue("playerId")
team = form.getvalue("team")
query = "DELETE FROM player_game_stats WHERE player_id = %s"
val = (playerId,)
cursor.execute(query, val)
cnx.commit()
query = "DELETE FROM player WHERE player_id = %s"
cursor.execute(query, val)
cnx.commit()
print('<html>')
print('<head>')
print('<title>View/Delete Players By Team</title>')
print('</head>')
print('<body>')
print('<p> Player deleted </p> <br>')
print('<a href="deleteOrViewPlayer.py?team=' + team + '&submitted=Submit"> View Changes </a>')
print('</body>')
print('</html>')
