# 并发
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

# 检测上面的三个socket是否连接成功了？谁 连接成功就给谁发信息
"""
知识点:
    client.setblocking(False)
    select.select检测:连接成功，数据回来了
    IO多路复用
    # 事件循环
    while True:
        r,w,e = select.select(socket_list,socket_list,[],0.05)
        # w是什么 [sk2,sk3],连接成功了
        for obj in w:
            obj.send(b'GET/http1.1\r\nhost:www.baidu.com\r\n\r\n')
        # r是什么？ [sk2,sk3],连接成功了要收数据了
        for obj in r:
        response = obj.recv(...) 
        print(response)
"""