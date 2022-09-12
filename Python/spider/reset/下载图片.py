import requests

url = 'https://res.pandateacher.com/2018-12-18-10-43-07.png'

res = requests.get(url)

pic = res.content

with open('./1.png', 'wb') as f:
    f.write(pic)
