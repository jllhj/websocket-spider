from flask import Flask,render_template,request
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
import json

app = Flask(__name__)

USERS = {
    '1':{'name':'东北','count':0},
    '2':{'name':'铁锤','count':0},
    '3':{'name':'贝贝','count':100},
}


@app.route('/index')
def index():
    return render_template('index.html',users=USERS)

WEBSOCKET_LIST = []
@app.route('/message')
def message():
    ws = request.environ.get('wsgi.websocket')
    if not ws:
        print('http')
        return '您使用的是http协议'
    WEBSOCKET_LIST.append(ws)
    while True:
        cid = ws.receive()
        if not cid:
            WEBSOCKET_LIST.remove(ws)
            ws.close()
            break
        old = USERS[cid]['count']
        new = old + 1
        USERS[cid]['count'] = new

        for client in WEBSOCKET_LIST:
            client.send(json.dumps({'cid':cid,'count':new}))


if __name__ == '__main__':
    http_server = WSGIServer(('127.0.0.1',5000),app,handler_class=WebSocketHandler)
    http_server.serve_forever()