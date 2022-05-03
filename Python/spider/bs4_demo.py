import requests
from bs4_demo import BeautifulSoup

res = requests.get(
    'https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')

html = res.text

soup = BeautifulSoup(html, 'html.parser')

items = soup.find_all(class_='books')

for item in items:
    kind = item.find('h2')
    title = item.find(class_='title')
    info = item.find(class_='info')

    print('%s， %s，%s' % (kind.text, title.text, info.text))
