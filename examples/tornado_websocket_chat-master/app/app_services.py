from tornado.ioloop import IOLoop
from app import app_factory
from app import app_cache as cache
from app.app_config import config


def run_dev_ioloop():
    """ Run Tornado IOLoop in debug mode (not for production). """
    app = app_factory.create_app(config)
    app.listen(config["port"])
    print("Running Tornado on", config["host"] + ":" + str(config["port"]))
    IOLoop.current().start()


def broadcast(message):
    """ Send json message to all clients registered to WebSocketHandler. """
    for client in cache.clients:
        client.write_message(message)
