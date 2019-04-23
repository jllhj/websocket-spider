import requests
import threading

urls = [
    'http://www.baidu.com/',
    'https://www.cnblogs.com/',
    'https://www.cnblogs.com/news/',
    'https://www.cn.bing.com/',
    'https://stackoverflow.com/',
]

def task(url):
    response = requests.get(url)
    print(response)

for url in urls:
    t = threading.Thread(target=task,args=(url,))
    t.start()

    # 缺点线程的利用率不高