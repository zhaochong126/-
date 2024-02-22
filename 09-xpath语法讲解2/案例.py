import requests
from lxml import etree

url = 'https://movie.douban.com/top250?start=0&headers=headers)result'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
}
resp = requests.get(url=url, headers=headers)
# print(resp.text)
tree = etree.HTML(resp.text)
divs = tree.xpath('//div[@class="info"]')
l1=[]
l2=[]
for div in divs:
    name = div.xpath('./div[@class="hd"]//span[@class="title"][1]/text()')
    score = div.xpath('./div[@class="bd"]/div[@class="star"]/span[2]/text()')
    l1.append(name)
    l2.append(score)

print(l1,l2)
with open('电影.txt','w',encoding='utf-8') as f:
    f.write(str(l1))
    f.write('\n')
    f.write(str(l2))

