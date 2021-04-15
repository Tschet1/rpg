#!/usr/bin/env python3

import socket
import sys
import time
import threading
from requests import get


def get_my_ip():
    return get('https://api.ipify.org').text


class Server(threading.Thread):
    def run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = get_my_ip()
        print(f"Server started successfully. IP is {ip}\n")

        hostname = ''
        port = 51712
        self.sock.bind((hostname, port))
        self.sock.listen(1)
        print(f"Listening on port {port}\n")

        (clientname, address) = self.sock.accept()

        print(f"Connection from {address}\n")

        while 1:
            chunk = clientname.recv(4096)
            print(f"{address}:{chunk}")


class Client(threading.Thread):
    def connect(self, host, port):
        self.sock.connect((host, port))

    def client(self, host, port, msg):
        sent = self.sock.send(msg.encode())
        print("Sent\n")

    def run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            host = input("Enter the hostname\n>>")
            port = int(input("Enter the port\n>>"))
        except EOFError:
            print("Error")
            return 1

        print("Connecting\n")
        s = ''
        self.connect(host, port)
        print("Connected\n")
        while 1:
            print("Waiting for message\n")
            msg = input('>>')
            if msg == 'exit':
                break
            if msg == '':
                continue
            print("Sending\n")
            self.client(host, port, msg)
        return(1)


if __name__ == '__main__':
    srv = Server()
    srv.daemon = True
    print("Starting server")
    srv.start()
    time.sleep(1)
    print("Starting client")
    cli = Client()
    print("Started successfully")
    cli.start()
