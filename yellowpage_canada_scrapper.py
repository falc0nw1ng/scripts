import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

print('Enter a location in Canada here')

location = input()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

def new_url(page, searchword, city):
    new_url = ('https://www.yellowpages.ca/search/si/{0}/{1}/{2}' .format(page, searchword, city))
    return new_url


parameter_file = open('query_parameters.txt', 'r')

for searchword in parameter_file.read().splitlines():
    f = csv.writer(open('%s-%s.csv'%(location,searchword),'w', newline=''))
    f.writerow(['Name', 'Address','Postal Code', 'City', ' Province', 'Number', 'Type'])
    print(searchword)
    for i in range(1,61):
        r = requests.get(new_url(i, searchword, location),headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        articles = soup.find_all('div', class_='listing__content__wrap--flexed jsGoToMp')
        if articles == []:
            print('End loop at page number {}\n'.format(i))
            break
        else:
            print('Currently on page number {}'.format(i))
            for items in articles:
                name = items.find('a', class_='listing__name--link listing__link jsListingName').text
                try:
                     address = items.find('span', class_='jsMapBubbleAddress' ,itemprop="streetAddress").text
                except:
                    address = ''
                try:
                    postalCode = items.find('span', class_='jsMapBubbleAddress', itemprop='postalCode').text
                except:
                    postalCode = ''
                try:
                    city = items.find('span', class_='jsMapBubbleAddress', itemprop='addressLocality').text
                except:
                    city = ''
                try:
                    province = items.find('span', class_='jsMapBubbleAddress', itemprop='addressRegion').text
                except:
                    province = ''
                try:
                    number = items.find('h4').text
                except:
                    number = ''
                f.writerow([name, address, postalCode, city, province, number, searchword])

print(location)















#parameters = open('query_parameters.txt', 'r')
#for i in parameters.read().splitlines():
#for items in articles:
#    website_tags = items.find('a', class_='mlr__item__cta')['href']
#    print(website_tags)
#
