from gevent import monkey; monkey.patch_all()
import gevent
# 协程 + IO切换
# pip3 install gevent
# gevent内部调用greenlet(实现了协程)

import requests
# 一个线程做的
def func(url):
    response = requests.get(url)
    print(response)

spawn_list = []

urls = [
    'http://www.baidu.com/',
    'https://www.cnblogs.com/',
    'https://www.cnblogs.com/news/',
    'https://www.cn.bing.com/',
    'https://stackoverflow.com/',
]
for url in urls:
    spawn_list.append(gevent.spawn(func,url))

gevent.joinall(spawn_list)