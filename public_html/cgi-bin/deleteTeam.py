#!/usr/bin/python3                                                                                                                                        

import mysql.connector, cgi
print("Content-type:text/html\r\n\r\n")
cnx = mysql.connector.connect(user='ptawil', password='ptawil', database='ptawil', host='localhost')

cursor = cnx.cursor()

form = cgi.FieldStorage()

teamId = form.getvalue("teamId")

query = "DELETE FROM player WHERE team_id = %s"
val = (teamId,)

cursor.execute(query, val)

query = "DELETE FROM team WHERE team_id = %s"

cursor.execute(query, val)

cnx.commit()

cursor.close()
cnx.close()
