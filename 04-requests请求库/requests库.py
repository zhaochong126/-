'''
默认请求头是{'User-Agent': 'python-requests/2.31.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

'''


import requests
url='https://www.baidu.com/'

# print(resp.text.encode('utf-8'))
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}
resp = requests.get(url=url, headers=headers)
with open('baidu.html','w',encoding='utf-8') as f:

    f.write(resp.text)
