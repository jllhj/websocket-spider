from .qb import client1

def done(response):
    print(response)

url_list = [
    {'host':'www.baidu.com','port':80,'path':'/','callback':done},# 如果想写入数据库 文本 自己定制回调函数done
    {'host': 'www.cnblogs.com', 'port': 80, 'path': '/','callback':done},
    {'host': 'www.bing.com', 'port': 80, 'path': '/','callback':done},
]

cl = client1()
for url in url_list:
    cl.add_request(url)

cl.run()