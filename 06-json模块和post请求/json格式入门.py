'''
eval去除字符串的引号
json.dumps()将python对象转换为json字符串
json.loads()将json字符串转为python对象
json.dump()将python中的对象转换成json对象存储到对象中
json.load()将json字符串转换为python对象提取出来
'''
import json

# 将json转换为对象
str1 = '{"name":"python"}'
l1=json.loads(str1)
print(l1)
print(type(l1))


# 将对象转为json
l2={'name': 'python'}
str2=json.dumps(l2)
print(str2)
print(type(str2))

str3='你好'
print(str3)

# 将对象转换为json字符串并写入对象
l3={'name': 'python','name1':'赵冲'}
f=open('1.json','w',)
json.dump(l3,f,ensure_ascii=False)# 中文不默认用Ascii编码写入

# 读取json文件
f=open('1.json','r')
result=json.load(f)
print(result,type(result))