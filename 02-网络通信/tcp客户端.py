'''
udp接收用recvfrom(),接收到的时元组类型(b'',(地址,端口号))
tcp用recv(),接收到的时二进制 b''
'''


from socket import *

# SOCK_STREAM时tcp协议
tcp_socket = socket(AF_INET, SOCK_STREAM)

ip_port = ('192.168.74.167',8080)
tcp_socket.connect(ip_port)

for i in range(10):
    data = '你好'+str(i)+'\n'
    tcp_socket.send(data.encode('gbk'))

res_data = tcp_socket.recv(1024)
print(res_data.decode('gbk'))
tcp_socket.close()