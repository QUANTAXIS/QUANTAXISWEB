from tornado.web import StaticFileHandler
from app.app_config import config
from app.app_handlers import IndexHandler
from app.app_handlers import ConnectionHandler
from app.app_handlers import DisconnectionHandler
from app.app_handlers import ChatHandler
from app.app_handlers import ResetHandler
from app.app_handlers import WebSocketHandler


urls = [
    (r"/", IndexHandler),
    (r"/connect", ConnectionHandler),
    (r"/disconnect", DisconnectionHandler),
    (r"/chat", ChatHandler),
    (r"/reset", ResetHandler),
    (r"/websocket", WebSocketHandler),
    (r'/(.*)', StaticFileHandler, {'path': config["static_path"]}),
]