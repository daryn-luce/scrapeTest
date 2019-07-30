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
    
def highest(data,stat,level=1):
    hold = 0
    champ = ''
    perlevel = stat + 'perlevel'
    if stat == 'movespeed' or stat == 'attackrange':
        bolperlevel = True
    else:
        bolperlevel = False
    for champion in data:
        if not(bolperlevel):
            if (data[champion]['stats'][stat] +(level * data[champion]['stats'][perlevel])) > hold:
                hold = data[champion]['stats'][stat] +(level * data[champion]['stats'][perlevel])
                champ = champion
                
        else:
            if data[champion]['stats'][stat] > hold:
                hold = data[champion]['stats'][stat]
                champ = champion
                print('here')
  
    return champ,stat,hold
    
def lowest(data,stat,level=1):
    hold = 1000
    champ = ''
    perlevel = stat + 'perlevel'
    if stat == 'movespeed' or stat == 'attackrange':
        bolperlevel = True
    else:
        bolperlevel = False
    for champion in data:
        if not(bolperlevel):
            if (data[champion]['stats'][stat] +(level * data[champion]['stats'][perlevel])) < hold:
                hold = data[champion]['stats'][stat] +(level * data[champion]['stats'][perlevel])
                champ = champion
                
        else:
            if data[champion]['stats'][stat] < hold:
                hold = data[champion]['stats'][stat]
                champ = champion
                print('here')
  
    return champ,stat,hold

    
#getAllChamp(data) #List all champions

level = 1 #change any level
champion = returnChamp(data, 'draven') # change any champion name
champStats = returnStat(champion)
name = champ(champion,'name') # list of values below
hname,hstat,hval = highest(data,'armor',level)
lname,lstat,lval = lowest(data,'armor',level)
ad = [stat(champStats,'attackdamage'),stat(champStats,'attackdamageperlevel')] # list of values below
totalad = levelStat(level,ad[0],ad[1])
# print('-----------------------------')
# print('{} - {}'.format(name,champ(champion,'blurb')))
# print('-----------------------------')
# print('{} has {} attack damage (+{} per level) base. At level {}, {} has {}'.format(name, ad[0],ad[1],level,name,totalad))
# print('-----------------------------')
print('-----------------------------')
print('{} has the highest base {} at level {} reaching {}'.format(hname,hstat,level,hval))
print('{} has the lowest base {} at level {} reaching {}'.format(lname,lstat,level,lval))

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