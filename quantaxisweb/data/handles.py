# coding:utf-8

import json

import tornado
from tornado.web import Application, RequestHandler, authenticated
from tornado.websocket import WebSocketHandler

from QUANTAXIS.QAFetch.QAQuery import QA_fetch_stock_day
from QUANTAXIS.QAFetch.QAQuery_Advance import QA_fetch_stock_day_adv


class BaseHandler(RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")


class Applications(Application):
    def __init__(self):
        handlers = [(r"/(\w+)", StockdayHandler)]
        Application.__init__(self, handlers, debug=True)


class StockdayHandler(BaseHandler):
    def get(self, data):

        self.write("Hello, world {}".format(data))


if __name__ == "__main__":
    app = Applications()
    app.listen(8829)
    tornado.ioloop.IOLoop.current().start()
