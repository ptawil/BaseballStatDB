#!/usr/bin/python3

import mysql.connector, cgi
print("Content-type:text/html\r\n\r\n")
cnx = mysql.connector.connect(user='ptawil', password='ptawil', database='ptawil', host='localhost')

cursor = cnx.cursor()

form = cgi.FieldStorage()
submit = form.getvalue("submitted")
if submit:
    team = form.getvalue("team").split(":")[0]
    query = "SELECT player_id, name, position FROM player JOIN team ON player.team_id = team.team_id WHERE team.team_id = %s"
    val = (team,)
    cursor.execute(query, val)
    print('<html>')
    print('<head>')
    print('<title>View/Delete Players By Team</title>')
    print('</head>')
    print('<body>')
    print('<table>')
    print('<tr> <th> Player Id </th> <th> Name </th> <th> Position </th> <th> Link to Delete </th> </tr>')
    for row in cursor:
        print('<tr>')
        print('<td>' + str(row[0]) + '</td>')
        print('<td>' + row[1] + '</td>')
        print('<td>' + row[2] + '</td>')
        print('<td> <a href="deletePlayer.py?playerId=' + str(row[0]) +'"> Delete Player </a> </td>')
        print('</tr>')
    print('</table>')
    print('</body>')
    print('</html>')
    
print('<html>')
print('<head>')
print('<title>View/Delete Players By Team</title>')
print('</head>')
print('<body>')
print('<form action="deleteOrViewPlayer.py">')
print('<select name="team">')
query="SELECT team_id,team_name from team"
cursor.execute(query)
for row in cursor:
    print('<option> ' + str(row[0]) + ':' + row[1] + '</option>')
print('</select>')
print('<input type="submit" name="submitted" value="Submit">')
print('</form>')
print('</body>')              
