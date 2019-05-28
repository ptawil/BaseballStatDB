#!/usr/bin/python3

import mysql.connector, cgi
print("Content-type:text/html\r\n\r\n")
cnx = mysql.connector.connect(user='ptawil', password='ptawil', database='ptawil', host='localhost')

cursor = cnx.cursor()

form = cgi.FieldStorage()
submit = form.getvalue("submitted")
if submit:
    team = form.getvalue("team").split(":")[0]
    query = "SELECT * FROM team WHERE team_id = %s"
    val = (team,)
    cursor.execute(query, val)
    print('<html>')
    print('<head>')
    print('<title>Add/Update a Team</title>')
    print('</head>')
    print('<body>')
    print('<table>')
    print('<tr> <th> Team Id </th> <th> Team City </th> <th> Team Name </th> <th> Stadium Name </th> <th> Link to Delete </th></tr>')
    for row in cursor:
        print('<tr>')
        print('<td>' + str(row[0]) + '</td>')
        print('<td>' + str(row[1]) + '</td>')
        print('<td>' + row[2] + '</td>')
        print('<td>' + row[3] + '</td>')
        print('<td> <a href="deleteTeam.py?teamId=' + str(row[0]) +'"> Delete Team </a> </td>')
        print('</tr>')
    print('</table>')

print('<html>')
print('<head>')
print('<title>Delete/View a Team</title>')
print('</head>')
print('<body>')
print('<form action="deleteOrViewTeam.py">')
print('Select a Team to View: <select name="team">')
query="SELECT team_id,team_name from team"
cursor.execute(query)
for row in cursor:
    print('<option> ' + str(row[0]) + ':' + row[1] + '</option>')
print('</select>')
print('<input type="submit" name="submitted" value="Submit">')
print('</form>')
print('</body>')
print('</html>')
