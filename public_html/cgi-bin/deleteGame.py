#!/usr/bin/python3                                                                            

import mysql.connector, cgi
print("Content-type:text/html\r\n\r\n")
cnx = mysql.connector.connect(user='ptawil', password='ptawil', database='ptawil', host='local\
host')                                                                                         
print('<html>')
print('<head>')                                                                                
print('<title>View Game Info</title>')                                                         
print('</head>')
print('<body>')
cursor = cnx.cursor()
form = cgi.FieldStorage()
game_id = form.getvalue('game_id')

query = "DELETE FROM player_game_stats WHERE game_id = %s"
val = (game_id,)
cursor.execute(query,val)

query = "DELETE FROM game WHERE game_id = %s"
cursor.execute(query, val)

cnx.commit()

print('<p> Game ' + game_id + ' was deleted. </p>')
print('<a href="viewOrDeleteGames.py"> See updated list of games. </a>')
print('</body>')
print('</html>')

cursor.close()
cnx.close()
