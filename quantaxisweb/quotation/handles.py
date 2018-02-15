# coding:utf-8

import tornado
from tornado.web import Application, RequestHandler, authenticated
from tornado.websocket import WebSocketHandler

"""
要实现2个api

1. SIMULATED WEBSOCKET

2. REALTIME WEBSOCKET

"""




class REALTIME(WebSocketHandler):
    def open(self):
        print('socket start')

    def on_message(self, message):
        self.write_message('message {}'.format(message))

    def on_close(self):
        print('connection close')
