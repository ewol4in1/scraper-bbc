from pprint import pprint
import re
import requests
from bs4 import BeautifulSoup

respone = requests.get(
    'https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt')


soup = BeautifulSoup(respone.text, 'lxml')
titles = soup.find_all(
    'span', {'class': 'lx-stream-post__header-text gs-u-align-middle'})

title_list = []
for title in titles:
    title_list.append(title.getText())


urls = soup.find_all('a', {'class': 'qa-heading-link lx-stream-post__header-link'})
for url in urls:
    print('https://www.bbc.com' + url.get('href'))

