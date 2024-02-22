import json

from jsonpath import jsonpath
dic ="""
{
    "name1": "school_info",
    "person_info": {
        "teachers": [
            {
                "id": "001",
                "name": "张三",
                "addr": "四川成都",
                "age": 25
            },
            {
                "id": "002",
                "name": "李四",
                "age": 28
            },
            {
                "id": "003",
                "name": "Mike",
                "addr": "广东深圳",
                "age": 16
            },
            {
                "id": "004",
                "name": "王哥",
                "addr": "广东广州",
                "age": 29
            }
        ],
        "students": [
            {
                "id": "001",
                "name": "毛毛",
                "age": 17,
                "addr": "湖南长沙"
            },
            {
                "id": "002",
                "name": "大树",
                "age": 27
            }
        ]
    },
    "avg": 25
}"""
# 将json格式转换为字典格式，jsonpath只能解析字典格式的数据
json_data = json.loads(dic)

# 用jsonpath解析出里面的name 格式是: $..节点
# print(jsonpath(json_data,'$..name'))
# print(jsonpath(json_data,'$..age'))

# 只想获取老师的名字
# teachers_names = jsonpath(json_data,'$..teachers')[0]
# for i in teachers_names:
#     print(i['name'])

# 利用通配符获取老师下的姓名
# teachers_names = jsonpath(json_data,'$..teachers[*].name')
# print(teachers_names)

# 条件筛选 $..节点[?(@.筛选条件)]
# print(jsonpath(json_data,'$..teachers[?(@.age>18 && @.addr=="广东广州")]'))

# 同时获得姓名和年龄,并写入字典
teachers = jsonpath(json_data,'$..teachers')[0]
# print(teachers)
dic = {}
for i in teachers:
    name = i['name']
    age = i['age']
    dic[name] = age

print(dic)