import os
from app import keys


APP_DIR = os.path.dirname(__file__)
STATIC_PATH = os.path.dirname(APP_DIR) + os.sep + "public"


config = {
    # Critical settings were externalized to keys.py file.
    "cookie_secret": keys.SECRET_KEY,
    "debug": keys.DEBUG,
    "login_url": "/",
    "host": keys.HOST,
    "port": 8000,
    "app_dir": APP_DIR,
    "static_path": STATIC_PATH
}
