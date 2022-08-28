#!/usr/bin/env python3

import unittest
import time
import multiprocessing
import queue
from communication.p2p import Server, Client


class TestCommunication_P2P(unittest.TestCase):
    def test_comm(self):
        srv = Server()
        srv.start()
        time.sleep(0.1)

        queue = multiprocessing.Queue()

        port=Server.PORT
        host="0.0.0.0"
        cli = Client(host=host, port=port, msgQueue=queue)
        print("Started successfully")
        cli.start()

        queue.put("Test case")

        cli.terminate()
        srv.terminate()
