import socket
import multiprocessing
import re
import mini_frame


class WSGIServer(object):
    def __init__(self):
        # 1. 创建套接字
        self.tcp_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 2. 绑定端口
        self.tcp_socket_server.bind(("", 7890))
        # 3. 将套接字设置为监听
        self.tcp_socket_server.listen(128)
        self.headers: list()
        self.status: str()

    def service_client(self, new_socket: socket.socket):
        # 为这个客户端返回数据
        # 1. 响应浏览器发送过来的HTTP请求
        request = new_socket.recv(1024)
        print(request)
        request_lines = request.splitlines()
        print("")
        print(">" * 20)
        print(request_lines)
        file_name = str()
        ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0].decode("gbk"))
        print(ret)
        if ret:
            print(ret)
            file_name = ret.group(1)
            print("-----------------------------------------------------------------------------")
            print(file_name)
            print("------------------------------------------------------------------------------")
            if file_name == "/":
                file_name = "/index.html"
        # 2. 返回HTTP格式的数据
        if not file_name.endswith(".py"):
            try:
                file_to_open = "./html" + file_name
                print(file_to_open)
                f = open(file_to_open, "rb")
            except:
                response = "HTTP/1.1 404 NOT FOUND \r\n"
                response += "\r\n"
                response += "-----------file not found---------- "
                new_socket.send(response.encode("gbk"))
            else:
                html_content = f.read()
                f.close()
                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"
                new_socket.send(response.encode("gbk"))
                new_socket.send(html_content)
        else:
            header = "HTTP/1.1 "
            header += self.status
            header += "\r\n"

            print(header)
            body = mini_frame.application({"test": "empty"}, self.set_start_response)
            response = header + body

            new_socket.send(response.encode("gbk"))
        new_socket.close()

    def set_start_response(self, status, headers):
        self.status = status
        self.headers = headers

    def run(self):
        # 4. 创建一个进程，为这个客服服务
        while True:
            # 4.1 拆包得到套接字和地址
            new_socket, client_addr = self.tcp_socket_server.accept()
            # 4.2 创建一个进程进行服务
            p = multiprocessing.Process(target=self.service_client, args=(new_socket,))
            p.start()
            new_socket.close()


def main():
    wsgi_server = WSGIServer()
    wsgi_server.run()


if __name__ == "__main__":
    main()
