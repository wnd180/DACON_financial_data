from pandas.io import html
import requests
from bs4 import BeautifulSoup
from os import name
import pandas as pd
from requests.api import request

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

for j in df_googlelink:
    req = requests.get(j)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
