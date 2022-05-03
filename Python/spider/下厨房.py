import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.xiachufang.com/explore/'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
res_foods = requests.get(url, headers=headers)

bs_foods = BeautifulSoup(res_foods.text, 'html.parser')

list = bs_foods.find_all(class_='name')

popular_foods = []

for item in list:
    tags = item.find_all('a')
    for tag in tags:
        popular_foods.append([tag.text.strip(), tag['href']])


with open('./food.csv', 'w+', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['菜名', '链接'])
    for item in popular_foods:
        writer.writerow(item)
