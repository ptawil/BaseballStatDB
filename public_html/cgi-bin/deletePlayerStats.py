#!/usr/bin/python3                                                                            

import mysql.connector, cgi
print("Content-type:text/html\r\n\r\n")
cnx = mysql.connector.connect(user='ptawil', password='ptawil', database='ptawil', host='localhost')                                                                                       
print('<html>')
print('<head>')                                                                               
print('<title>Delete Player Stats</title>')                                                   
print('</head>')
print('<body>')
cursor = cnx.cursor()
form = cgi.FieldStorage()
player_id = str(form.getvalue('player_id'))
game_id = str(form.getvalue('game_id'))

query = "DELETE FROM player_game_stats WHERE player_id = %s AND game_id = %s"

vals = (player_id, game_id)
cursor.execute(query, vals)

cnx.commit()

print('<p> Player ' + player_id + ' in game ' + game_id + ' was deleted. </p>')
print('<a href="viewGameStats.py?game_id=' + game_id + '"> View updated game stats </a>') 
print('</body>')
print('</html>')
