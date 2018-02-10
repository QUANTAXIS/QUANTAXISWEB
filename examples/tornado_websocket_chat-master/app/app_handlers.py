import json
from tornado.web import RequestHandler
from tornado.web import authenticated
from tornado.websocket import WebSocketHandler
from app import app_cache as cache
from app import app_services as services
from app.app_config import config


class BaseHandler(RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")


class IndexHandler(BaseHandler):
    def get(self):
        if self.current_user:
            self.redirect("/chat")
        else:
            with open(config["static_path"] + "/index.html", 'r') as file:
                self.write(file.read())


class ConnectionHandler(BaseHandler):
    def post(self):
        try:
            # If Javascript is enabled -> JSON is posted
            username = json.loads(self.request.body.decode())["username"]
        except:
            # If Javascript is disabled -> form is posted
            username = self.get_argument("username")
        if username and (username not in cache.users):
            self.set_secure_cookie("user", username)
            cache.users[username] = username
            self.redirect("/chat")
            message = {
                "code": "msg",
                "username": "HOST",
                "text": username + " connected"
            }
            message = json.dumps(message)
            services.broadcast(message)
        else:
            self.redirect("/")


class DisconnectionHandler(BaseHandler):
    @authenticated
    def get(self):
        username = self.current_user.decode()
        self.set_secure_cookie("user", "")
        try:
            del cache.users[username]
        except KeyError:
            pass
        message = {
            "code": "msg",
            "username": "HOST",
            "text": username + " disconnected"
        }
        message = json.dumps(message)
        services.broadcast(message)
        return self.redirect("/")


class ChatHandler(BaseHandler):
    @authenticated
    def get(self):
        if self.current_user:
            with open(config["static_path"] + "/chat.html", 'r') as file:
                self.write(file.read())
        else:
            self.redirect("/")


class WebSocketHandler(WebSocketHandler):

    def open(self):
        cache.clients.add(self)

    def on_message(self, message):
        message = json.loads(message)
        if message['code'] == 'msg':
            message['username'] = self.get_secure_cookie("user").decode()
            cache.messages.append(message)
            message = json.dumps(message)
            [client.write_message(message) for client in cache.clients]
        elif message['code'] == 'msgs':
            message['messages'] = cache.messages
            self.write_message(json.dumps(message))

    def on_close(self):
        cache.clients.remove(self)


class ResetHandler(RequestHandler):
    """ Clear cached messages. """

    def get(self):
        cache.messages = []
        self.redirect("/")
