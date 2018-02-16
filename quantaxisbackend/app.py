# coding:utf-8

import tornado
from tornado.web import Application, RequestHandler, authenticated
from quantaxisbackend.data.handles import StockdayHandler, StockminHandler
from quantaxisbackend.quotation.handles import RealtimeSocketHandler, SimulateSocketHandler
from quantaxisbackend.user.handles import SigninHandler, SignupHandler
from quantaxisbackend.util.handles import BaseHandler


class INDEX(BaseHandler):
    def get(self):
        self.render("index.html")


if __name__ == '__main__':
    app = Application(
        handlers=[
            (r"/", INDEX),
            (r"/stock/day", StockdayHandler),
            (r"/stock/min", StockminHandler),
            (r"/user/signin", SigninHandler),
            (r"/user/signup", SignupHandler),
            (r"/realtime", RealtimeSocketHandler),
            (r"/simulate", SimulateSocketHandler)
        ],
        debug=True
    )
    app.listen(8010)
    tornado.ioloop.IOLoop.instance().start()
