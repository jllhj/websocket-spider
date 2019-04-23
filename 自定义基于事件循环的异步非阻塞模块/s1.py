# 阻塞的
# import socket
# client = socket.socket()
# client.connect(('www.baidu.com',80))
# client.send(b'GET/http1.1\r\nhost:www.baidu.com\r\n\r\n')
#
# response = client.recv(1024)
# print(response)
# client.close()


# import socket
# client = socket.socket()
# print('连接开始')
# client.connect(('www.google.com',80)) # 阻塞
# print('连接结束')
# client.send(b'GET/http1.1\r\nhost:www.baidu.com\r\n\r\n')
#
# response = client.recv(1024)
# print(response)
# client.close()


# 非阻塞
import socket
client = socket.socket()
client.setblocking(False)

client.connect(('www.baidu.com',80)) # 阻塞

# 想办法获取socket状态，已连接成功之后才往下走
print('连接结束')
client.send(b'GET/http1.1\r\nhost:www.baidu.com\r\n\r\n')

# 想办法回去socket状态 是否将数据返回了
response = client.recv(1024)
print(response)
client.close()