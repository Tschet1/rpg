#!/usr/bin/env python3

import socket
import time
import multiprocessing
import atexit
from requests import get


def get_my_ip():
    return get('https://api.ipify.org').text


class Server(multiprocessing.Process):
    PORT= 51712

    def __init__(self, *args, **kwargs):
        super().__init__(args=args, kwargs=kwargs)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        ip = get_my_ip()
        print(f"Server started successfully. IP is {ip}\n")

        hostname = ''
        self.sock.bind((hostname, self.PORT))
        self.sock.listen(1)
        print(f"Listening on port {self.PORT}\n")

        (clientname, address) = self.sock.accept()

        print(f"Connection from {address}\n")

        while 1:
            chunk = clientname.recv(4096)
            print(f"{address}:{chunk}")

    def terminate(self):
        self.sock.close()
        super().terminate()


class Client(multiprocessing.Process):
    def __init__(self, host, port, msgQueue: multiprocessing.Queue, *args, **kwargs):
        super().__init__(args=args, kwargs=kwargs)
        self.host = host
        self.port = port
        self.queue = msgQueue
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        self.sock.connect((host, port))

    def client(self, host, port, msg):
        sent = self.sock.send(msg.encode())
        print("Sent\n")

    def run(self):
        print("Connecting\n")
        s = ''
        self.connect(self.host, self.port)
        print("Connected\n")
        while 1:
            print("Waiting for message\n")
            msg = self.queue.get(True)
            if msg == 'exit':
                break
            if msg == '':
                continue
            print("Sending\n")
            self.client(self.host, self.port, msg)
        return(1)

    def terminate(self):
        self.sock.close()
        super().terminate()


if __name__ == '__main__':
    srv = Server()
    print("Starting server")
    srv.start()
    time.sleep(1)
    print("Starting client")
    try:
        host = input("Enter the hostname\n>>")
        port = int(input("Enter the port\n>>"))
    except EOFError as e:
        print("Error")
        print(e)

    queue = multiprocessing.Queue()
    cli = Client(host=host, port=port, msgQueue=queue)
    print("Started successfully")
    cli.start()

    def __cleanup():
        print("Terminate")
        srv.terminate()
        cli.terminate()

    atexit.register(__cleanup)

    while(True):
        msg = input('>>')
        queue.put(msg)
