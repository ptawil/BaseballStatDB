#!/usr/bin/python3                                                                                                                                         

import mysql.connector, cgi
print("Content-type:text/html\r\n\r\n")
cnx = mysql.connector.connect(user='ptawil', password='ptawil', database='ptawil', host='localhost')

cursor = cnx.cursor()

form = cgi.FieldStorage()
playerId = form.getvalue("playerId")

query = "DELETE FROM player WHERE player_id = %s"
val = (playerId,)
cursor.execute(query, val)
cnx.commit()
print('<html>')
print('<head>')
print('<title>View/Delete Players By Team</title>')
print('</head>')
print('<body>')
print('<p> Player deleted </p> <br>')
print('<a href="deleteOrViewPlayer.py"> Back to View/Delete Players </a>')
print('</body>')
print('</html>')
