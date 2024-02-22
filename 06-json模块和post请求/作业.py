import json
import requests

url = 'https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=1&num=40&sort=symbol&asc=1&node=hs_bjs&symbol=&_s_r_a=init'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}

resp = requests.get(url=url, headers=headers)
resp_obj = json.loads(resp.text)
# print(resp_obj)
list=[1,2,3,4,5,6,7,8]




with open('作业.txt','w',encoding='utf-8') as f:
    for i in resp_obj:
        list[0]=i['name']
        list[1]=i['sell']
        list[2]=i['pricechange']
        list[3]=i['changepercent']
        list[4]=i['buy']
        list[5]=i['sell']
        list[6]=i['settlement']
        list[7]=i['open']
        print(list)
        f.write(str(list))
        f.write('\n')


