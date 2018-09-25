# -*- coding: utf-8 -*-
"""
Authors: Jason Teng
2018-9-24

This file contains the server code for CS 5700 Project 1
"""

import asyncore, socket

TCP_HOSTNAME = "cs5700f18.ccs.neu.edu"
TCP_PORT = 27993

NUID = "001876580"

INITIAL_MESSAGE = "cs5700fall2018 HELLO " + NUID + "\n" 

class TCPClient(asyncore.dispatcher):

    BUFFER_SIZE = 1024

    def __init__(self, address):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect(address)
        print "connected"
        self.send(INITIAL_MESSAGE)
        print "sent"

    def handle_connect(self):
        pass

    def handle_close(self):
        self.close()
        
    def readable(self):
        pass

    def handle_read(self):
        print "can read"
        self.data = self.recv(BUFFER_SIZE)
        print self.data

    def writable(self):
        pass

    def handle_write(self):
        pass


client = TCPClient((TCP_HOSTNAME, TCP_PORT))
asyncore.loop()