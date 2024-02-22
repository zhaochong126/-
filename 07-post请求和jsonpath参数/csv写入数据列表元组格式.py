import csv
# 列表元组格式
data = [('肖申克的救赎', '9.7', '希望让人自由'), ('霸王别姬', '9.6', '风华绝代'), ('阿甘正传', '9.5', '一部美国近现代史')]
head = ('电影名','评分','经典台词')
with open('电影.csv','w',encoding='utf-8-sig') as f:
    # 写入对象
    write = csv.writer(f)
    # 写入表头
    write.writerow(head)
    # 写入表格内容
    write.writerows(data)