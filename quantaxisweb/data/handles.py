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
        handlers = [(r"/stock/day", StockdayHandler)]
        Application.__init__(self, handlers, debug=True)

#/(\w*)


class StockdayHandler(BaseHandler):
    def get(self):
        print(self.request.arguments)

        code = self.request.arguments.get('code', '000001')
        start = str(self.request.arguments.get('start', '2017-01-01'))
        end = str(self.request.arguments.get('end', '2017-12-31'))
        print(code[0].decode('utf-8'))
        print(start)
        print(end)
        data = QA_fetch_stock_day(code[0].decode(
            'utf-8'), start, end, format='json')

        print(data)


        self.write({'result':data,'status':200})


if __name__ == "__main__":
    app = Applications()
    app.listen(8829)
    tornado.ioloop.IOLoop.current().start()
