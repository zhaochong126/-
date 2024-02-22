str1 = 'hello'
str2 = '你好'
print(len(str1.encode('utf-8')))#5
print(len(str2.encode('utf-8')))#6
print(len(str1[0].encode('utf-8')))#1
print(len(str2[0].encode('utf-8')))#3