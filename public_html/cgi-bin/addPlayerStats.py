#!/usr/bin/python3                                                           

import mysql.connector, cgi
print("Content-type:text/html\r\n\r\n")
cnx = mysql.connector.connect(user='ptawil', password='ptawil', database='ptawil', host='localhost')
print('<html>')
print('<head>')
print('<title>Add Game Info</title>')
print('</head>')
print('<body>')
cursor = cnx.cursor()
form = cgi.FieldStorage()
count = int(form.getvalue('numOfPlayers'))
game_id = form.getvalue('game_id')
for i in range(1,count):
    checked = form.getvalue('player' + str(i))
    if checked == "on":
        player_id = form.getvalue('playerInfo' + str(i)).split(" ")[0] 
        runs = form.getvalue('runs' + str(i))
        atBats = form.getvalue('num_of_abs' + str(i))
        hits = form.getvalue('num_of_hits' + str(i))
        homeruns = form.getvalue('homeruns' + str(i))
        query = "INSERT INTO player_game_stats (player_id, game_id, num_of_at_bats, num_of_hits, num_of_runs, num_of_homeruns) VALUES (%s, %s, %s, %s, %s, %s)"
        vals = (player_id, game_id, atBats, hits, runs, homeruns)
        cursor.execute(query, vals)
        cnx.commit()
        print('<p> Added ' + player_id + ' into the database </p>')
print('<a href="addGameInfo.py"> Record another game </a>')
print('<br>')
print('<a href="../baseball.html"> Back to home page </a>')
print('</body>')
print('</html>')
