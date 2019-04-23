#  Twisted

from twisted.web.client import getPage, defer
from twisted.internet import reactor


def stop_loop(arg):  # 停止循环
    reactor.stop()


def get_response(contents):
    print(contents)


deferred_list = []

url_list = [
    'http://www.baidu.com/',
    'https://www.cnblogs.com/',
    'https://www.cnblogs.com/news/',
    'https://www.cn.bing.com/',
    'https://stackoverflow.com/',
]

for url in url_list:
    deferred = getPage(bytes(url, encoding='utf8'))
    deferred.addCallback(get_response)
    deferred_list.append(deferred)

dlist = defer.DeferredList(deferred_list) # 监听是否完成了 完成了就执行下面
dlist.addBoth(stop_loop)

reactor.run()