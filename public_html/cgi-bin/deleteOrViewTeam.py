#!/usr/bin/python3

import mysql.connector, cgi
print("Content-type:text/html\r\n\r\n")
cnx = mysql.connector.connect(user='ptawil', password='ptawil', database='ptawil', host='localhost')

cursor = cnx.cursor()
print('<html>')
print('<head>')
print('<title>View/Delete a Team</title>')
print('</head>')
print('<body>')

query = "SELECT team_id, team_city, team_name, stadium_name, wins(team_id), losses(team_id) FROM team"
cursor.execute(query)
print('<table>')
print('<tr> <th> Team Id </th> <th> Team City </th> <th> Team Name </th> <th> Stadium Name </th> <th> Number of Wins </th> <th> Number of Losses </th> <th> Link to Delete </th></tr>')
for row in cursor:
    print('<tr>')
    print('<td>' + str(row[0]) + '</td>')
    print('<td>' + str(row[1]) + '</td>')
    print('<td>' + row[2] + '</td>')
    print('<td>' + row[3] + '</td>')
    print('<td>' + str(row[4]) + '</td>')
    print('<td>' + str(row[5]) + '</td>')
    print('<td> <a href="deleteTeam.py?teamId=' + str(row[0]) +'"> Delete Team </a> </td>')
    print('</tr>')
print('</table>')

print('<a href="../baseball.html"> Back to home page </a>')
print('</body>')
print('</html>')
