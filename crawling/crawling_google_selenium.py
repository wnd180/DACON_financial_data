import pandas as pd
from bs4 import BeautifulSoup
import requests
from urllib.parse import quote_plus
from selenium import webdriver

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
# for i in df_googlelink:
#     # response = requests.get(i)
#     # soup = BeautifulSoup(response.text, 'html.parser')
#     # finding_html = soup.find('div', class_ = 'yuRUbf')
#     # link = finding_html.find('a')
#     # print(link.get_text().strip())

#     # requested01 = requests.get(i)
#     # test_1 = BeautifulSoup(requested01.text, 'html.parser')
#     # result01_class01 = test_1.find('div', class_ = 'yuRUbf')
#     # result01_class02 = result01_class01.find('a')
#     # print(result01_class01.get_text())

#     # response = requests.get(i)
#     # if response.status_code == 200:
#     #     html = response.text
#     #     soup = BeautifulSoup(html, 'html.parser')
#     #     request_class = soup.find('div', class_ = 'yuRUbf')
#     #     request_class2 = request_class.find('a')
#     #     print(request_class2.get_text().strip())

#     htmls = requests.get(i)
#     bs = BeautifulSoup(htmls.content, 'html.parser')
#     Search_data = bs.find('a', class_='yuRUbf')
#     print(Search_data)

for i in df_googlelink:
    driver = webdriver.Chrome(
        executable_path=r'/Users/kwonseongjung/Downloads/chromedriver')
    driver.get(i)
    html = driver.page_source
    soup = BeautifulSoup(html)
    # v = soup.select('.yuRUbf')
    # for j in v:
    #     print(j.select_one('.LC20lb.DKV0Md').text)  # 제목
    #     print(j.a.attrs['href'])       # 링크
    #     print()
    v = soup.select_one('.yuRUbf')
    # for j in v:
    #     print(j.select_one('.LC20lb.DKV0Md').text)  # 제목
    #     print(j.a.attrs['href'])       # 링크
    #     print()
    detail_urls.append(v.a.attrs['href'])
