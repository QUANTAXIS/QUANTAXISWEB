def create_app(config):
    from app.app_urls import urls
    from tornado.web import Application
    app = Application(urls, **config)
    return app
