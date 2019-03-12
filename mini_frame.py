import time


def log_in():
    return "Here is log_in() time is %s" % time.ctime()


def register():
    return "Here is register() time is %s" % time.ctime()


def profile():
    return "Here is profile() time is %s" % time.ctime()


def application(file_name: str()):
    if file_name == "/log_in.py":
        return log_in()
    elif file_name == "/register.py":
        return register()

    elif file_name == "/profile.py":
        return profile()
    else:
        return "%s" % time.ctime()

# def application(env, make_header):
#     make_header("200 OK", [("Content-Type", "text/html")])
#     return "这是application的返回"
