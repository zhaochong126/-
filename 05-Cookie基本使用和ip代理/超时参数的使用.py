import requests


# timeout设置最长连接时长,如果没有连接到则报错
url = 'https://github.com/'
resp = requests.get(url=url,timeout=3)
print(resp.text)