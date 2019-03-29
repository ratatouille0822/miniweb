import time


def response_index():
    with open("./templates/index.html", "rb") as f:
        content = f.read()
        f.close()
        ret = bytes.decode(content)
        return ret


def response_center():
    with open("./templates/center.html", "rb") as f:
        content = f.read()
        f.close()
        ret = bytes.decode(content)
        return ret


def application(env, set_response_header):
    if env["FILE_PATH"] == "/index.py":
        set_response_header("200 OK \r\n", [("Content-Type", "text/html;charset=utf-8"), ])
        return response_index()

    elif env["FILE_PATH"] == "/center.py":
            set_response_header("200 OK \r\n", [("Content-Type", "text/html;charset=utf-8"), ])
            return response_center()

    else:
        set_response_header("404 NOT FOUND \r\n", [("Content-Type", "text/html;charset=utf-8"), ])
        return "%s" % time.ctime()
