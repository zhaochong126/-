import requests

url = 'https://fanyi.so.com/index/search?'
query = {
    'eng':1,
    'validate':'',
    'ignore_trans':'',
    'query':input()
}

headers={
    'Pro':'fanyi',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}
resp = requests.post(url,data=query,headers=headers)
print(resp.json()['data']['fanyi'])
