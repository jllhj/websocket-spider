import socket
import select


class Request(object):
    def __init__(self,sock,info):
        self.sock = sock
        self.info = info

    def fileno(self):
        return self.sock.fileno()

class client1(object):
    def __init__(self):
        self.sock_list = []
        self.conns = []

    def add_request(self,req_info):
        """
        创建请求
        req_info = {'host':'www.baidu.com','port':80,'path':'/'},
        :return:
        """
        sock = socket.socket()
        sock.setblocking(False)
        try:
            sock.connect((req_info['host'],req_info['port']))
        except BlockingIOError as e:
            pass

        obj = Request(sock,req_info)
        self.sock_list.append(obj)
        self.conns.append(obj)

    def run(self):
        """
        开始事件循环 检测:连接成功？数据是否返回？
        :return:
        """
        while True:
            # select.select([socket对象,])
            # 可是任何对象,对象一定要fileno方法
            # 对象.fileno()
            # select.select([request对象,])
            r,w,e = select.select(self.sock_list,self.conns,[],0.05) # 最大超时时间
            # w 是否连接成功
            for obj in w:
                # 检查obj是哪个字典
                # 检查request对象
                # socket,{'host':'www.baidu.com','port':80,'path':'/'}
                data = "GET %s http/1.1\r\nhost:%s\r\n\r\n"%(obj.info['path'],obj.info['host'])
                obj.sock.send(data.encode('utf-8'))
                # 检查避免重复发两次 应该删掉
                self.conns.remove(obj)
            # 数据返回 接收到数据
            for obj in r:
                response = obj.sock.recv(8096)
                # print(obj.info['host'],response)
                obj.info['callback'](response)
                self.sock_list.remove(obj)

            # 所有请求已经返回
            if not self.sock_list:
                break