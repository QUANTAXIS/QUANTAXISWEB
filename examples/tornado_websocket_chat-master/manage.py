from app import app_services as services


commands = {
    "runserver": services.run_dev_ioloop
}


if __name__ == "__main__":
    import sys
    commands[sys.argv[1]]()