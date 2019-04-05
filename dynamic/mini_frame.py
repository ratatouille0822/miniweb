import time
import re

URL_LIST = dict()


def route(url):
    def select_func(func):
        URL_LIST[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return select_func


@route("/index.py")
def response_index():
    with open("./templates/index.html", "rb") as f:
        content = f.read()
        f.close()
        ret = bytes.decode(content)
        return ret


@route("/center.py")
def response_center():
    with open("./templates/center.html", "rb") as f:
        content = f.read()
        content_to_send = bytes.decode(content)
        f.close()
        content_to_send = re.sub(r"\{%content%\}", "这里是Center ", content_to_send)
        print(content_to_send)
        ret = content_to_send
        return ret


# SELECT_FUNC = \
#     {
#         "/index.py": response_index,
#         "/center.py": response_center
#     }


def application(env, set_response_header):
    file_name = env["FILE_PATH"]
    # if env["FILE_PATH"] == "/index.py":
    #     return response_index()
    #
    # elif env["FILE_PATH"] == "/center.py":
    #     set_response_header("200 OK \r\n", [("Content-Type", "text/html;charset=utf-8"), ])
    #     return response_center()
    #
    # else:
    #     set_response_header("404 NOT FOUND \r\n", [("Content-Type", "text/html;charset=utf-8"), ])
    #     return "%s" % time.ctime()
    if file_name in URL_LIST:
        set_response_header("200 OK \r\n", [("Content-Type", "text/html;charset=utf-8"), ])
        func = URL_LIST[file_name]
    else:
        return str(time.time())
    return func()
