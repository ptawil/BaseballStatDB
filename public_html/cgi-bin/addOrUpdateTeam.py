#!/usr/bin/python3                                                                                                                                         
import mysql.connector, cgi
print("Content-type:text/html\r\n\r\n")
cnx = mysql.connector.connect(user='ptawil', password='ptawil', database='ptawil', host='localhost')

cursor = cnx.cursor()

form = cgi.FieldStorage()
submit = form.getvalue("submitted")
if submit:
    city = form.getvalue("city")
    teamName = form.getvalue("teamName")
    stadium = form.getvalue("stadiumName")
    if form.getvalue("action") == "add":
        query = "INSERT INTO team (team_city, team_name, stadium_name) VALUES (%s, %s, %s)"
        val = (city, teamName, stadium)
        cursor.execute(query, val)
        cnx.commit()
    else:
        teamId = form.getvalue("team").split(":")[0]
        query = "UPDATE team SET "
        params = []
        if city:
           query+="team_city = %s"
           params.append(city)
        if teamName:
            if len(params) == 1:
                query+=","    
            query+="team_name = %s"
            params.append(teamName)
        if stadium:
            if len(params) > 0:
                query+=","
            query+="stadium_name = %s"
            params.append(stadium)

        query += " WHERE team_id = %s"
        params.append(teamId)
        val = tuple(params)
        cursor.execute(query, val)
        cnx.commit()
        
print('<html>')
print('<head>')
print('<title>Add/Update a Team</title>')
print('</head>')
print('<body>')
print('<form action="addOrUpdateTeam.py">')
print('<input type="radio" name="action" value="add">Add a team <br>')
print('Team City: <input type="text" name="city"> <br>')
print('Full Team Name: <input type="text" name="teamName"> <br>')
print('Stadium Name: <input type="text" name="stadiumName"> <br>')
print('<input type="radio" name="action" value="update">Update Team Info <br>')
print('Select a Team to Update: <select name="team">')
query="SELECT team_id,team_name from team"
cursor.execute(query)
for row in cursor:
    print('<option> ' + str(row[0]) + ':' + row[1] + '</option>')
print('</select>')
print('<input type="submit" name="submitted" value="Submit">')
print('</form>')
print('<a href="../baseball.html"> Back to home page </a>')
print('</body>')
print('</html>')
cursor.close()
cnx.close()
