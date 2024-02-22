import requests
name=input('亲输入你要搜索的科目:')
url='https://www.sogou.com/web'
params={
    'query':name
}
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}

resp = requests.get(url=url,params=params,headers=headers)

with open(name+'.html','w',encoding='utf-8') as f:
    f.write(resp.text)
    print('over')