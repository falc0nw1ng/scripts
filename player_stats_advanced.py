import pandas as pd
from bs4 import BeautifulSoup
from requests import get
import csv
import codecs

#####3 requires print(row.encode('utf8'))
# start by scraping one page at a time
# year indicates the ending year, so 2020 would be the 2019-2020 season
# seasons =  range(2000,2020)

f = csv.writer(open('nba_advanced_2020.csv', 'w', newline=''))
f.writerow(['Player', 'Pos', 'Age', 'Tm', 'G', 'Per', 'TS%', '3PAr', 'TFr', 'ORB%', 'DRB%', 'TRB%',
'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'OWS', 'DWS', 'WS', 'OBPM', 'DBPM', 'BPM', 'VORP', 'Season'])

bball_refference_stat = 'advanced'
seasons = range(2020,2021)
for season in seasons:
    url = ("https://www.basketball-reference.com/leagues/NBA_{0}_{1}.html" .format(season, bball_refference_stat))
    response = get(url)
    soup = BeautifulSoup(response.content,'html.parser',)
    rows = soup.find_all('tr', class_='full_table')
    for row in rows:
        name = row.find('td', {'data-stat':'player'}).text.encode('utf8')
        position = row.find('td', {'data-stat':'pos'}).text
        age = row.find('td', {'data-stat':'age'}).text
        team = row.find('td', {'data-stat':'team_id'}).text
        games = row.find('td', {'data-stat':'g'}).text
        per = row.find('td', {'data-stat':'per'}).text
        ts_pct = row.find('td', {'data-stat':'ts_pct'}).text
        fg3a_r = row.find('td', {'data-stat':'fg3a_per_fga_pct'}).text
        fta_r = row.find('td', {'data-stat':'fta_per_fga_pct'}).text
        orb_pct = row.find('td', {'data-stat':'orb_pct'}).text
        drb_pct = row.find('td', {'data-stat':'drb_pct'}).text
        trb_pct = row.find('td', {'data-stat':'trb_pct'}).text
        ast_pct = row.find('td', {'data-stat':'ast_pct'}).text
        stl_pct = row.find('td', {'data-stat':'stl_pct'}).text
        blk_pct = row.find('td', {'data-stat':'blk_pct'}).text
        tov_pct = row.find('td', {'data-stat':'tov_pct'}).text
        usg_pct = row.find('td', {'data-stat':'usg_pct'}).text
        ows = row.find('td', {'data-stat':'ows'}).text
        dws = row.find('td', {'data-stat':'dws'}).text
        ws = row.find('td', {'data-stat':'ws'}).text
        OBPM = row.find('td', {'data-stat':'obpm'}).text
        DBPM = row.find('td', {'data-stat':'dbpm'}).text
        BPM = row.find('td', {'data-stat':'bpm'}).text
        vorp = row.find('td', {'data-stat':'vorp'}).text



        f.writerow([name, position, age, team, games, per, ts_pct, fg3a_r, fta_r, orb_pct, drb_pct, trb_pct, ast_pct, stl_pct, blk_pct, tov_pct, usg_pct, ows, dws, ws, OBPM, DBPM, BPM, vorp, season])


'''
for row in rows:
    columns = row.find_all('td')
    for col in columns:
        name = col
        print(col.text.encode('utf-8'))

'''
#print(rows.content)
#for row in rows:
#    n

#print(table)

















































#
