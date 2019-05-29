#!/usr/bin/python3                                                                            

import mysql.connector, cgi
print("Content-type:text/html\r\n\r\n")
cnx = mysql.connector.connect(user='ptawil', password='ptawil', database='ptawil', host='localhost')                                                                                        
print('<html>')
print('<head>')
print('<title>Update Player Info</title>')                                                   
print('</head>')
print('<body>')
cursor = cnx.cursor()
form = cgi.FieldStorage()
player_id = form.getvalue('player_id')
name = form.getvalue('name')
position = form.getvalue('position')
team = form.getvalue('team')
team_id = team.split(":")[0]
query = "UPDATE player SET name = %s, position= %s, team_id = %s WHERE player_id = %s"
vals = (name, position, team_id, player_id)
cursor.execute(query, vals)
cnx.commit()
print('<p> Player ' + player_id + ' was updated. </p>')
print('<a href="deleteOrViewPlayer.py?team=' + team + '&submitted=Submit"> See update </a>')
print('</body>')
print('</html>')
cursor.close()
cnx.close()
