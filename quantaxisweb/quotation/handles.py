# coding:utf-8
import os
import tornado
from tornado.web import Application, RequestHandler, authenticated
from tornado.websocket import WebSocketHandler
import QUANTAXIS as QA
import time
"""
要实现2个api

1. SIMULATED WEBSOCKET

2. REALTIME WEBSOCKET

"""


class INDEX(RequestHandler):
    def get(self):
        self.render("index.html")


class REALTIME(WebSocketHandler):
    def open(self):
        print('socket start')

    def on_message(self, message):
        self.write_message('message {}'.format(message))

    def on_close(self):
        print('connection close')


class SIMULATED(WebSocketHandler):
    def open(self):
        self.write_message('start')

    def on_message(self, message):
        if len(str(message)) == 6:
            data = QA.QA_util_to_json_from_pandas(
                QA.QA_fetch_stock_day(message, '2017-01-01', '2017-12-31', 'pd'))
            for item in data:
                self.write_message(item)
                time.sleep(0.2)

    def on_close(self):
        print('connection close')


if __name__ == '__main__':
    app = Application(
        handlers=[
            (r"/", INDEX),
            (r"/realtime", REALTIME),
            (r"/simulate", SIMULATED)
        ],
        debug=True
    )
    app.listen(8010)
    tornado.ioloop.IOLoop.instance().start()
