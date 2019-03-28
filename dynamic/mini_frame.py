import time



def log_in():
    return "Here is log_in() time is %s" % time.ctime()


def register():
    return "Here is register() time is %s" % time.ctime()


def profile():
    return "Here is profile() time is %s" % time.ctime()


def application(env: dict(), set_response_hesder):
    if env["FILE_PATH"] == "/index.py":
        with open("./templates/index.html", "rb") as f:
            content = f.read()
            print(content)
            f.close()
            set_response_hesder("200 OK \r\n", [("Content-Type", "text/html;charset=utf-8"), ])
            return content

    elif env["FILE_PATH"] == "/register.py":
        set_response_hesder("200 OK \r\n", [("Content-Type", "text/html;charset=utf-8"), ("server", "My SVR")])
        return register()

    elif env["FILE_PATH"] == "/profile.py":
        set_response_hesder("200 OK \r\n", [("Content-Type", "text/html;charset=utf-8"), ])
        return profile()

    elif env["FILE_PATH"] == "/center.py":
        with open("./templates/center.html", "rb") as f:
            content = f.read()
            f.close()
            set_response_hesder("200 OK \r\n", [("Content-Type", "text/html;charset=utf-8"), ])
            return content

    else:
        set_response_hesder("404 NOT FOUND \r\n", [("Content-Type", "text/html;charset=utf-8"), ])
        return "%s" % time.ctime()
