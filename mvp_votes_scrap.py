import pandas as pd
from bs4 import BeautifulSoup
from requests import get
import csv
import codecs

#####3 requires print(row.encode('utf8'))
# start by scraping one page at a time
# year indicates the ending year, so 2020 would be the 2019-2020 season
# seasons =  range(2000,2020)

f = csv.writer(open('mvp_votes.csv', 'w', newline=''))
f.writerow(['Player', 'Age', 'First', 'PTs Won', 'PTs Max', 'Share', 'G', 'MP', 'PTs', 'TRB', 'AST', 'STL', 'BLK',
'FG%', '3P%', 'FT%', 'WS', 'WS/48', 'Season'])

seasons = range(1980,2021)
for season in seasons:
    url = ("https://www.basketball-reference.com/awards/awards_{}.html" .format(season))
    response = get(url)
    soup = BeautifulSoup(response.content,'html.parser',)
    table = soup.find('tbody')
    rows = table.find_all('tr')
    for row in rows:
        name = row.find('td', {'data-stat':'player'}).text.encode('utf8')
        age = row.find('td', {'data-stat':'age'}).text
        first = row.find('td', {'data-stat':'votes_first'}).text
        pts_won = row.find('td', {'data-stat':'points_won'}).text
        pts_max = row.find('td', {'data-stat':'points_max'}).text
        share = row.find('td', {'data-stat':'award_share'}).text
        games = row.find('td', {'data-stat':'g'}).text
        mp = row.find('td', {'data-stat':'mp_per_g'}).text
        pts = row.find('td', {'data-stat':'pts_per_g'}).text
        trb = row.find('td', {'data-stat':'trb_per_g'}).text
        ast = row.find('td', {'data-stat':'ast_per_g'}).text
        stl = row.find('td', {'data-stat':'stl_per_g'}).text
        blk = row.find('td', {'data-stat':'blk_per_g'}).text
        fg = row.find('td', {'data-stat':'fg_pct'}).text
        three_fg = row.find('td', {'data-stat':'fg3_pct'}).text
        ft = row.find('td', {'data-stat':'ft_pct'}).text
        ws = row.find('td', {'data-stat':'ws'}).text
        ws_per_48 = row.find('td', {'data-stat':'ws_per_48'}).text

        f.writerow([name, age, first, pts_won, pts_max, share, games, mp,
         pts, trb, ast, stl, blk, fg, three_fg, ft, ws, ws_per_48, season])


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
