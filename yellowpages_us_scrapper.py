import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

def new_url(searchterm, location, page):
    base_url = ('https://www.yellowpages.com/search?search_terms={0}&geo_location_terms={1}&page={2}'.format(searchterm, location, page))
    return base_url


location_text = open('location.txt','r')

for location in location_text.read().splitlines():
    f = csv.writer(open('%s-ebikes.csv'%(location), 'w', newline=''))
    f.writerow(['Name', 'Categories', 'Website', 'Number', 'Address', 'Location', 'Search Term'])
    for searchterm in ['ebikes', 'electric bikes']:
        for page in range(1,30):
            r = requests.get(new_url(searchterm, location, page),headers=headers)
            soup = BeautifulSoup(r.content, 'html.parser')
            articles = soup.find_all('div', class_='info')
            if articles == []:
                print("Loop ends at page {0} for {1} in {2}" .format(page, searchterm, location))
                break
            else:
                for item in articles:
                    try:
                        name = item.find('a', class_='business-name').text
                    except:
                        name = ''
                    try:
                        categories = item.find('div', class_='categories').text
                    except:
                        categories = ''
                    try:
                        website = item.find('a', class_='track-visit-website')['href']
                    except:
                        website = ''
                    try:
                        number = item.find('div', class_='phones phone primary').text
                    except:
                        number = ''
                    try:
                        address = item.find('div', class_='street-address').text
                    except:
                        address = ''
                    try:
                        locality = item.find('div', class_='locality').text
                    except:
                        locality = ''
                    f.writerow([name, categories, website, number, address, locality, searchterm])














#
