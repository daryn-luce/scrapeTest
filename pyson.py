import json
import requests

response = requests.get('https://ddragon.leagueoflegends.com/cdn/9.14.1/data/en_US/champion.json')
todos = json.loads(response.text)

print(todos['data']['Anivia']['blurb'])
