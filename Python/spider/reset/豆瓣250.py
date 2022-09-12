import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'}

res = requests.get(url, headers=headers)

html = BeautifulSoup(res.text, 'html.parser')

info = html.find_all(class_='info')

for item in info:
    title = item.find(class_='title')
    point = item.find(class_='rating_num')
    print(title.text, point.text)
