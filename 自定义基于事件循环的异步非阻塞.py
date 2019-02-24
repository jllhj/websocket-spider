import socket

client1 = socket.socket()
client1.setblocking(False) # 不阻塞

try:
    client1.connect(('www.baidu.com',80)) #端口
except BlockingIOError as e:
    pass

client2 = socket.socket()
client2.setblocking(False) # 不阻塞

try:
    client2.connect(('www.baidu.com',80)) #端口
except BlockingIOError as e:
    pass


client3 = socket.socket()
client3.setblocking(False) # 不阻塞

try:
    client3.connect(('www.baidu.com',80)) #端口
except BlockingIOError as e:
    pass

###############################
# 检测上述的socket是否连接成功了 谁连接成功给谁发
# 想办法获取socket状态，已连接成功之后才往下走
client1.send(b'GET/http1.1\r\nhost:www.baidu.com\r\n\r\n')

client.send(b'GET/http1.1\r\nhost:www.baidu.com\r\n\r\n')

# 想办法获取socket状态，是否将数据返回了
response = client.recv(8096)
print(response)

client.close()

# 等价于爬虫内部
# import requests
# response = requests.get('www.baidu.com')
