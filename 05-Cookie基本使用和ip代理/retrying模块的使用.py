import requests
from retrying import retry


# stop_max_attempt_number=4,最大重试次数为4

@retry(stop_max_attempt_number=4)
def f1(url):
    print('请求')
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }
    resp = requests.get(url=url,headers=headers)
    if resp.status_code==200:
        return resp.text


url = 'https://www.baidu.com'
baidu_html=f1(url)
print(baidu_html)