import time


def log_in():
    return "Here is log_in() time is %s" % time.ctime()


def register():
    return "Here is register() time is %s" % time.ctime()


def profile():
    return "Here is profile() time is %s" % time.ctime()


def application(env: dict(), set_response_hesder):
    if env["FILE_PATH"] == "/log_in.py":
        set_response_hesder("200 OK \r\n", [("Content-Type", "text/html;charset=utf-8"), ])
        return log_in()
    elif env["FILE_PATH"] == "/register.py":
        set_response_hesder("200 OK \r\n", [("Content-Type", "text/html;charset=utf-8"), ("server", "My SVR")])
        return register()
    elif env["FILE_PATH"] == "/profile.py":
        set_response_hesder("200 OK \r\n", [("Content-Type", "text/html;charset=utf-8"), ])
        return profile()
    else:
        set_response_hesder("404 NOT FOUND \r\n")
        return "%s" % time.ctime()
