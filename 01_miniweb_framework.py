import multiprocessing
import socket
import re


def service_client():
    pass

def main():
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2. 绑定
    tcp_server_socket.bind(("", 7890))
    # 3. 设置为监听
    tcp_server_socket.listen(1024)
    while True:
        # 4. 接受客户连接
        new_soccket, client_addr = tcp_server_socket.accept()
        print(client_addr)
        # 5. 为这个客户服务
        p = multiprocessing.Process(target=service_client, args=(new_soccket,))
        p.start()
        new_soccket.close()


if __name__ == "__main__":
    main()
