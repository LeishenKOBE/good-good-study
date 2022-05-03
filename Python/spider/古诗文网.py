import requests

from bs4 import BeautifulSoup

url = 'https://so.gushiwen.cn/shiwens/default.aspx?page=1&tstr=&astr=%E8%8B%8F%E8%BD%BC&cstr=&xstr='

res = requests.get(url)

poems = BeautifulSoup(res.text, 'html.parser')

cards = poems.find_all(class_="sons")

for card in cards:
    print(card)
