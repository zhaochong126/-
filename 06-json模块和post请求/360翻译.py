import requests

url = 'https://fanyi.so.com/index/search?'
name = input('你要翻译的单词是:')
query = {
    'eng':1,
    'validate':'',
    'ignore_trans':'',
    'query':name
}

# 判断eng取值eng=1英译汉,eng=0汉译英
if len(name[0].encode('utf-8'))==3:
    query['eng']=0

headers={
    'Pro':'fanyi',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}
resp = requests.post(url,data=query,headers=headers)
print(resp.json()['data']['fanyi'])
