import csv

data = [
    {'title': '肖申克的救赎', 'star': '9.7', 'quote': '希望让人自由'},
    {'title': '霸王别姬', 'star': '9.6', 'quote': '风华绝代'},
    {'title': '阿甘正传', 'star': '9.5', 'quote': '一部美国近现代史'}
]
# 设置表头信息
head = ('title', 'star', 'quote')
'''
ValueError: dict contains fields not in fieldnames:
字典格式写入数据：字典的key要跟表头保持一致
'''
# 保存数据
with open('douban1.csv', 'w', encoding='utf-8-sig', newline='') as f:
    # 1. 创建csv写入对象  fieldnames: 设置表头的参数
    writer = csv.DictWriter(f, fieldnames=head)
    # 2. 写入表头
    writer.writeheader()
    # 3. 写入数据
    writer.writerows(data)
