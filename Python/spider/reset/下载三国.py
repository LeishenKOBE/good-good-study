import requests

res = requests.get(
    'https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')

novel = res.text

with open('./三国演义第一回.md', 'a+', encoding='utf-8') as f:
    f.write(novel)
