import requests

urls = [
    'http://www.baidu.com/',
    'https://www.cnblogs.com/',
    'https://www.cnblogs.com/news/',
    'https://www.cn.bing.com/',
    'https://stackoverflow.com/',
]

for url in urls:
    response = requests.get(url=url)
    print(response)