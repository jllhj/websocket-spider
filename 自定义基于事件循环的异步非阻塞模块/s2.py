import socket
client = socket.socket()
client.setblocking(False)
try:
    client.connect(('www.baidu.com',80)) # 阻塞
except BlockingIOError as e:
    pass
# 想办法获取socket状态，已连接成功之后才往下走
print('连接结束')
client.send(b'GET/http1.1\r\nhost:www.baidu.com\r\n\r\n')

# 想办法回去socket状态 是否将数据返回了
response = client.recv(1024)
print(response)
client.close()