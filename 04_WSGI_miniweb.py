import multiprocessing
from dynamic import mini_frame
import re
import socket


class WSGIServer(object):
    def __init__(self):
        # 创建套接字：
        self.new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.new_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 1. 绑定端口
        # port = sys.argv[1]
        # print("Current port binding is %s" % port)
        self.new_socket.bind(("", 7890), )
        # 2. 设置监听
        self.new_socket.listen(1024)
        self.header = str()
        self.body = str()
        self.env = dict()
        self.item_name = list()
        self.item_content = list()

    def start_svr(self, new_socket: socket.socket):
        request = new_socket.recv(1024)
        request_line = request.splitlines()
        print(request_line)
        file_name = "./templates"
        file_request = re.match(r"[^/]+(/[^ ]*)", request_line[0].decode("gbk")).group(1)
        if file_request == "/":
            file_request = "/index.html"
        if file_request.endswith(".css") or file_request.endswith(".js"):
            file_name = "./static"
        file_name += file_request
        print(file_name)

        if not file_request.endswith(".py"):
            # 如果是静态资源，在此处理：
            try:
                f = open(file_name, "rb")
            except:
                content = "HTTP/1.1 404 not found\r\n"
                content += "\r\n"
                content += "页面丢了"
                new_socket.send(content.encode("gbk"))
            else:
                content = f.read()
                f.close()
                print("&" * 200)
                # print(content)
                header = "HTTP/1.1 200 OK \r\n"
                header += "\r\n"
                new_socket.send(header.encode("gbk"))
                new_socket.send(content)
        else:
            # 动态资源请求：
            # header = "HTTP/1.1 200 OK \r\n"
            # header += "\r\n"
            self.env["FILE_PATH"] = file_request
            body = mini_frame.application(self.env, self.set_response_header)
            response = self.header + "\r\n" + body
            new_socket.send(response.encode("utf-8"))

    def set_response_header(self, http_status: str(), info):
        self.header = "HTTP/1.1 "
        self.header += http_status
        for temp in info:
            self.header += "%s:%s\r\n" % (temp[0], temp[1])

    def run(self):
        while True:
            new_socket, client_ip_addr = self.new_socket.accept()
            p = multiprocessing.Process(target=self.start_svr, args=(new_socket,))
            p.start()
            new_socket.close()


def main():
    svr = WSGIServer()
    svr.run()
    pass


if __name__ == "__main__":
    main()
