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
player_id = form.getvalue('player_id')
game_id = form.getvalue('game_id')
atBats = form.getvalue('num_of_abs')
hits = form.getvalue('num_of_hits')
runs = form.getvalue('num_of_runs')
homeruns = form.getvalue('num_of_homeruns')
query = "UPDATE player_game_stats SET num_of_at_bats = %s, num_of_hits = %s, num_of_runs = %s, num_of_homeruns = %s WHERE player_id = %s AND game_id = %s"
vals= (atBats, hits, runs, homeruns, player_id, game_id)
cursor.execute(query, vals)
cnx.commit()
print('<p> Player ' + player_id + ' in game ' + game_id + ' was updated. </p>')
print('<a href="viewGameStats.py?game_id=' + game_id + '"> See updated stats for this game </a>')
print('</body>')
print('</html>')
