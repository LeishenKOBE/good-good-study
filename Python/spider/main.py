import requests

url = 'https://www.sogou.com/'

response = requests.get(url=url)

page_text = response.text

with open('./sogou.html', 'w', encoding='utf-8') as f:
    f.write(page_text)

print('爬取数据完毕')
