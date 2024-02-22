from socket import *
tcp_socket = socket(AF_INET, SOCK_STREAM)

# 设置端口复用,程序退出,端口号需要释放
tcp_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)
ip_port = ('', 8080)
tcp_socket.bind(ip_port)

# 设置监听
tcp_socket.listen(128)
a, b =tcp_socket.accept()
# print(a)
res_data=a.recv(1024).decode('gbk')
print(res_data)
tcp_socket.close()