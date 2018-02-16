# coding:utf-8

import datetime
import json

import tornado
from tornado.web import Application, RequestHandler, authenticated
from tornado.websocket import WebSocketHandler

from QUANTAXIS.QAFetch.QAQuery import QA_fetch_stock_day
from QUANTAXIS.QAFetch.QAQuery_Advance import QA_fetch_stock_day_adv
from QUANTAXIS.QAUtil.QATransform import QA_util_to_json_from_pandas


class BaseHandler(RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")


class StockdayHandler(BaseHandler):
    def get(self):
        """
        采用了get_arguents来获取参数
        默认参数: code-->000001 start-->2017-01-01 end-->today

        """
        code = self.get_argument('code', default='000001')
        start = self.get_argument('start', default='2017-01-01')
        end = self.get_argument('end', default=str(datetime.date.today()))
        data = QA_util_to_json_from_pandas(
            QA_fetch_stock_day(code, start, end, format='pd'))

        self.write({'result':data})


if __name__ == "__main__":

    app = Application(
        handlers=[
            (r"/stock/day", StockdayHandler)
        ],
        debug=True
    )
    app.listen(8010)
    tornado.ioloop.IOLoop.current().start()
