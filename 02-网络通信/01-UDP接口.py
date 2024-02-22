from socket import *
udp = socket(AF_INET,SOCK_DGRAM)
# AF_INET是ipv4地址类型
# SOCK_DGRAM是使用UDP通信
addr=('192.168.74.167', 8080)
# 自定义地址
loc_addr = ('192.168.74.167',7799)
# 绑定端口号
udp.bind(loc_addr)
data = input('请输入要发送的数据:')

udp.sendto(data.encode('gbk'),addr)
rec_data = udp.recvfrom(1024)
print(rec_data[0].decode('gbk'))
# 在通信时通常带有汉字的使用gbk，英文和其他语言一般是用utf-8
udp.close()
