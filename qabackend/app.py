# coding:utf-8

import tornado
from tornado.web import Application, RequestHandler, authenticated
from data.handles import StockdayHandler, StockminHandler
from quotation.handles import RealtimeSocketHandler, SimulateSocketHandler
from user.handles import SigninHandler, SignupHandler

class INDEX(RequestHandler):
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
