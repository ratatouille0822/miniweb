import socket
import multiprocessing
import re


def service_client(new_socket : socket.socket):
    # 为这个客户端返回数据
    # 1. 响应浏览器发送过来的HTTP请求
    request = new_socket.recv(1024)
    request_lines = request.splitlines()
    print("")
    print(">" * 20)
    print(request_lines)

    file_name = str()
    ret = re.match(r"[^/] + (/[^ ])", request_lines[0])
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"

    # 2. 返回HTTP格式的数据

    try:
        f = open("./html" + file_name, rb)
    except:
        response = "HTTP/1.1 404 NOT FOUND \r\n"
        response += "\r\n"
        response += "-----------file not found---------- "
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        new_socket.send(response.encode("utf-8"))
        new_socket.send(html_content)

    new_socket.close()

    pass

def main():
    # 1. 创建套接字
    tcp_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    # 2. 绑定端口
    tcp_socket_server.bind(("",7890))
    # 3. 将套接字设置为监听
    tcp_socket_server.listen(128)
    # 4. 创建一个进程，为这个客服服务
    while True:
        # 4.1 拆包得到套接字和地址
        new_socket, client_addr = tcp_socket_server.accept()
        # 4.2 创建一个进程进行服务
        p = multiprocessing.Process(target=service_client,args=(new_socket, ))
        p.start()
        new_socket.close()

if __name__ == "__main__":
    main()