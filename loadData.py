#!/usr/bin/python3 

import requests

mlbUrl = "http://lookup-service-prod.mlb.com/json/named.team_all_season.bam"

PARAMS = {'season':'2019','all_star_sw': '\'N\'', 'sport_code': '\'mlb\''}

r = requests.get(url = mlbUrl, params=PARAMS)
data = r.json()
teamInfo = data['team_all_season']['queryResults']['row']

mlbRosterUrl = "http://lookup-service-prod.mlb.com/json/named.roster_40.bam"
playerFile = open("players.txt", "w")
teamFile = open("teams.txt","w")
teamId = 0
playerId=0
for team in teamInfo:
    teamFile.write(str(teamId) + "\t" + team['city'] + "\t" + team['name_display_full'] + "\t" + team['venue_name'] + "\n")
    param = {'team_id': team['team_id']}
    response = requests.get(url = mlbRosterUrl, params=param)
    roster = response.json()['roster_40']['queryResults']['row']
    for player in roster:
        playerFile.write(str(playerId) + "\t" + player['name_display_first_last'] + "\t" + player['position_txt'] + "\t" + str(teamId)+"\n")
        playerId +=1
    teamId+=1

    
