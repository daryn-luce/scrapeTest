import requests
from bs4 import BeautifulSoup

page = requests.get('https://na.leagueoflegends.com/en/game-info/champions/Aatrox/')
soup = BeautifulSoup(page.content, 'html.parser')

content = soup.find(class_='content-border')
stats = content.find_all(class_='gs-container')
label = stats[1].find_all(class_='stat-label')
value = stats[1].find_all(class_='stat-value')

print(label[0].get_text()[:-1])
print(value[0].get_text())
