'''
https://httpbin.org/ip:查看外网ip
ipip.net:同理
本机IP地址:39.148.15.166
在requests模块中忽略证书的参数是verify=False
禁止重定向参数是allow_redirects=False 重定向状态码是302(临时重定向),301(永久重定向)
'''


import requests

url='https://httpbin.org/ip'
proxy={
    'https':'115.195.248.120:17394'
}
resp = requests.get(url=url,proxies=proxy)
print(resp.text)