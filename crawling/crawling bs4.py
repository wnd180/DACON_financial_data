from os import name
import pandas as pd
from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen

pd.options.display.float_format = '{:.5f}'.format
pd.options.display.float_format = '{:,.0f}'.format

df = pd.read_csv(
    "/Users/kwonseongjung/Desktop/univ/2-2/재정데이터 시각화 경진대회/crawling/종합 예산 시계열-년도_열-한글단위열 추가.csv")
google = 'https://www.google.com/search?q='
google_link = []


df_detail = df['세부사업']

for i in df_detail:
    goolink = google+i
    google_link.append(goolink)
df['googlelink'] = google_link

detail_urls = []
df_googlelink = df['googlelink']
for i in df_googlelink:

    # response = requests.get(i)
    # if response.status_code == 200:
    #     html = response.text
    #     soup = BeautifulSoup(html, 'html.parser')
    #     request_class = soup.find('div', class_ = 'yuRUbf')
    #     request_class2 = request_class.find('a')
    #     print(request_class2.get_text().strip())

    response = requests.get(i)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.find('yuRUbf')
    print(name)

    # 여기서부터 css selector
    # response = requests.get(i)
    # html = response.text
    # soup = BeautifulSoup(html, 'html.parser')
    # name = soup.select('#rso > div:nth-child(1) > div')
    # print(name)

df['detaillink'] = detail_urls
df.to_csv('/Users/kwonseongjung/Downloads', index=None)
