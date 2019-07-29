import json
import requests

response = requests.get('https://ddragon.leagueoflegends.com/cdn/9.14.1/data/en_US/champion.json')
todos = json.loads(response.text)
data = todos['data']


def returnChamp(data,name):
    try:
        for d in data:
            if d.lower() == name.lower():
                return data[d]
    except:
        print('Invalid Champion')

def returnStat(champion):
    return champion['stats']

def getAllChamp(data):
    for champion in data:
        print(champion)
        
def champ(champion,val):
    try:
        return champion[val]
    except:
        print('Wrong value')

def stat(stat,val):
    try:
        return stat[val]
    except:
        print('Wrong value')

def levelStat(level,base,per):
    return (level * per) + base

#getAllChamp(data) #List all champions

level = 12 #change any level
champion = returnChamp(data, 'singed') # change any champion name
champStats = returnStat(champion)
name = champ(champion,'name') # list of values below
ad = [stat(champStats,'attackdamage'),stat(champStats,'attackdamageperlevel')] # list of values below
totalad = levelStat(level,ad[0],ad[1])
print('-----------------------------')
print('{} - {}'.format(name,champ(champion,'blurb')))
print('-----------------------------')
print('{} has {} attack damage (+{} per level) base. at level {}, {} has {}'.format(name, ad[0],ad[1],level,name,totalad))


### values for champ(champion, value) method
 # version
 # id
 # key
 # name
 # title
 # blurb
 # info *
 # tags *
 # partype
 # stats*

### values for stat(stat,values) method
# hp
# hpperlevel
# mp
# mpperlevel
# movespeed
# armor
# armorperlevel
# spellblock
# spellblockperlevel
# attackrange
# hpregen
# hpregenperlevel
# mpregen
# mpregenperlevel
# crit
# critperlevel
# attackdamage
# attackdamageperlevel
# attackspeedperlevel
# attackspeed