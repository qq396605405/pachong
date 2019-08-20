import requests
import pandas as pd
from bs4 import BeautifulSoup
res=requests.get('https://china.nba.com/static/data/league/playerstats_All_All_All_0_All_false_2018_4_All_Team_points_All_perGame.json')
json_player = res.json()
players=json_player['payload']['players']
names=['姓名','助攻','篮板','得分']
player_lists=[]
for player in players:
    print('姓名%s'%player['playerProfile']['displayName'])
    print('场均助攻%s'%player['statAverage']['assistsPg'])
    print('场均篮板%s'%player['statAverage']['rebsPg'])
    print('场均得分%s'%player['statAverage']['pointsPg'])
    player_lists.append([player['playerProfile']['displayName'],player['statAverage']['assistsPg'],player['statAverage']['rebsPg'],player['statAverage']['pointsPg']])

test=pd.DataFrame(columns=names,data=player_lists)
test.to_excel('data of players.xlsx')