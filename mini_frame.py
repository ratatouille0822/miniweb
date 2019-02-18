import time


def log_in():
    return "Here is log_in() time is %s" % time.ctime()


def register():
    return "Here is register() time is %s" % time.ctime()


def application(file_name: str()):
    if file_name == "log_in.py":
        return log_in()
    elif file_name == "register.py":
        return register()
    else:
        return "%s" % time.ctime()
