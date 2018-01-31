#!/Python27/python

print "Content-Type: text/html"
print ""

import cgi
import cgitb
cgitb.enable()

print "<html><head></head><body>"

form = cgi.FieldStorage()
if "names" not in form:
    print "<H1>Error</H1>"
    print "Names of players not specified."
    raise SystemExit
else:
    names = form["names"].value
    #for name in names.split(", "):
    #    print name + "</br>"

#########################
#       SCRAPING        #
#########################
import urllib2
from bs4 import BeautifulSoup

player_tanks_dict = {}

for name in names.split(", "):
    response = urllib2.urlopen("http://www.noobmeter.com/player/na/" + name)
    content = response.read()

    soup = BeautifulSoup(content, "html")
    table = soup.find("table",{"class":"tablesorter"})
    row = table.findAll("tr")[20]
    tanks = row.findAll("span")

    player_tanks = []
    for tank in tanks:
        x = tank.text.lstrip()
        player_tanks.append(x[:-1])

    player_tanks_dict[name] = player_tanks

#print player_tanks_dict

#player_tanks_dict = {'Strikker23': [u'Object 140', u'Centurion Action X', u'T50 51', u'Object 430', u'Maus'], 'CHAZ746': [u'Bat Chatillon 25 t', u'Leopard 1', u'T62A', u'T50 51', u'STB-1', u'M48A5 Patton', u'Object 140', u'121', u'AMX 30B', u'E-50 Ausf. M', u'T-100 LT', u'AMX 13 105', u'WZ-132-1', u'XM551 Sheridan', u'Rheinmetall Panzerwagen', u'T92', u'Object 261', u'IS-7', u'T57 Heavy', u'AMX 50B', u'113', u'T110E5', u'WZ-111 model 5A', u'IS-4', u'Kranvagn', u'Object 260', u'E-100', u'G121 Grille 15 L63', u'Strv 103B', u'FV215b (183)', u'Object 268', u'Badger', u'Object 263'], 'twofourcharlie': [u'Bat Chatillon 155', u'Object 261', u'JagdPz E-100', u'Object 268', u'FV215b (183)', u'T110E4', u'T110E3', u'Strv 103B', u'Badger', u'FV4005 Stage II', u'Centurion Action X', u'E-50 Ausf. M', u'M48A5 Patton', u'Maus', u'E-100', u'T57 Heavy', u'IS-7', u'IS-4', u'113', u'FV215b', u'T110E5', u'Pz.Kpfw. VII', u'Super Conqueror', u'Type 5 Heavy'], 'Cheng_Qi': [u'Object 140', u'M48A5 Patton', u'E-100', u'JagdPz E-100'], 'ACandieCaneKilling': [u'T50 51', u'STB-1', u'T62A', u'Object 140', u'M48A5 Patton', u'Centurion Action X', u'Object 430', u'T110E4', u'G121 Grille 15 L63', u'JagdPz E-100', u'FV215b (183)', u'AMX 50 Foch 155', u'AMX 50 Foch B', u'Badger', u'T110E5', u'IS-4', u'113', u'IS-7', u'T57 Heavy', u'FV215b', u'E-100', u'Kranvagn', u'WZ-111 model 5A', u'Maus', u'Super Conqueror', u'AMX 50B'], 'dirtyscot': [u'Bat Chatillon 25 t', u'T62A', u'Centurion Action X', u'E-50 Ausf. M', u'Object 140', u'121', u'Object 261', u'Bat Chatillon 155', u'Waffentr\xe4ger auf E 100', u'T110E4', u'FV215b (183)', u'G121 Grille 15 L63', u'AMX 50 Foch 155', u'T110E3', u'AMX 50 Foch B', u'Badger', u'AMX 13 105', u'E-100', u'T57 Heavy', u'Maus', u'IS-7', u'113', u'AMX 50B', u'T110E5', u'IS-4', u'WZ-111 model 5A', u'Object 260'], 'Water_Is_Wet': [u'M60', u'T50 51', u'Object 430', u'Leopard 1', u'Bat Chatillon 25 t', u'G121 Grille 15 L63', u'Strv 103B', u'Rheinmetall Panzerwagen', u'T57 Heavy'], 'XiangPotato': [u'Bat Chatillon 25 t', u'E-50 Ausf. M', u'Bat Chatillon 155', u'Object 261', u'T92', u'Object 268', u'T57 Heavy', u'T110E5', u'IS-7', u'E-100', u'IS-4'], 'goldtooth1': [u'T92', u'T110E4', u'FV215b (183)', u'T110E3', u'Badger', u'E-100', u'Super Conqueror', u'IS-7'], 'Howitzer_666': [u'Bat Chatillon 25 t', u'M48A5 Patton', u'Object 140', u'Leopard 1', u'T50 51', u'T-100 LT', u'Conqueror Gun Carriage', u'113', u'WZ-111 model 5A', u'E-100', u'Maus', u'Pz.Kpfw. VII']}

#########################
#       ALGORITHM       #
#########################

#Tanks that commander wants
tanks_desired = []
if "tank8" not in form:
    #only 7 tanks
    for x in range(1,8):
        tanks_desired.append(form["tank" + str(x)].value)
else:
    if "tank11" not in form:
        #only 10 tanks
        for x in range(1,11):
            tanks_desired.append(form["tank" + str(x)].value)
    else:
        #only 15 tanks
        for x in range(1,16):
            tanks_desired.append(form["tank" + str(x)].value)

tanks_desired_dict = {}
for tank in tanks_desired:
    tanks_desired_dict[tank] = tanks_desired.count(tank)

"""print "Needed: "
print tanks_desired_dict
print "</br>"""

#Calculate tanks that players have
tanks_actual_dict = {}
player_amount_tanks = {}

for player in player_tanks_dict:
    #print "Player: " + player + "</br>"
    for tank in tanks_desired_dict:
        if tank in player_tanks_dict[player]: #player has tank
            #print "- " + tank + "</br>"
            if tank in tanks_actual_dict:
                tanks_actual_dict[tank] = tanks_actual_dict[tank] + 1
            else:
                tanks_actual_dict[tank] = 1
            if player in player_amount_tanks:
                player_amount_tanks[player] = player_amount_tanks[player] + 1
            else:
                player_amount_tanks[player] = 1
                
"""print "Tanks Available: "                
print tanks_actual_dict
print "</br>"
print "Player Tanks: "
print player_amount_tanks
print "</br>"""



#Variables
players_selected = {}
available_players = []
for player in player_tanks_dict:
    available_players.append(player)

#Player has no tanks that are needed
for player in player_tanks_dict:
    if player not in player_amount_tanks:
        players_selected[player] = "Random"
        available_players.remove(player)

"""print "Available players: "
print available_players
print "</br>"""

#If one tank doesnt have enough players
for tank in tanks_desired_dict:
    if tanks_actual_dict[tank] < tanks_desired_dict[tank]:
        #print tank + " does not have enough players</br>"
        for player in player_tanks_dict:
            if player in available_players:
                #print "Checking " + player + "</br>"
                if tank in player_tanks_dict[player]: #player has tank that is needed
                    #print "Removing " + player + "</br>"
                    available_players.remove(player)
                    players_selected[player] = tank
                    tanks_desired_dict[tank] = tanks_desired_dict[tank] - 1

#Players with 1 tank
temp_list = []
"""print "Available players: "
print available_players
print "</br>"""

for player in available_players:
    #print "Working with player: " + player + "</br>"
    if player_amount_tanks[player] < 2: #player has one or no tanks relevant
        for tank in tanks_desired_dict:
            if tank in player_tanks_dict[player]: #player has tank
                temp_list.append(player)
                players_selected[player] = tank
                if tanks_desired_dict[tank] == 0:
                    #put player in first spot available
                    for tank in tanks_desired_dict:
                        if tanks_desired_dict[tank] > 0:
                            tanks_desired_dict[tank] = tanks_desired_dict[tank] - 1
                            break
                else:
                    tanks_desired_dict[tank] = tanks_desired_dict[tank] - 1

for player in temp_list:
    available_players.remove(player)

#Remaining players from smallest amt. of tanks to highest
if len(available_players) > 0:
    while len(available_players) > 0:
        lowest_player = available_players[0]
        for player in available_players:
            if player_amount_tanks[player] < player_amount_tanks[lowest_player]:
                lowest_player = player
        for tank in tanks_desired_dict:
            if tanks_desired_dict[tank] > 0:
                if tank in player_tanks_dict[lowest_player]:
                    players_selected[lowest_player] = tank
                    available_players.remove(lowest_player)
                    tanks_desired_dict[tank] = tanks_desired_dict[tank] - 1
                    break
            
            
"""print "Players Selected: "
print players_selected
print "</br>"
print "Players Available: "
print available_players
print "</br>"""

print "<table>"

for player in players_selected:
    print "<tr><td>" + player + "</td><td>" + players_selected[player] + "</td></tr>"

print "</table>"    
    
print "</body></html>"
