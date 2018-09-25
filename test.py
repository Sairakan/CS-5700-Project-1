# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 12:35:47 2018

@author: akari
"""

import socket

TCP_HOSTNAME = "cs5700f18.ccs.neu.edu"
TCP_PORT = 27993

BUFFER_SIZE = 1024
NUID = "001876580"

INITIAL_MESSAGE = "cs5700fall2018 HELLO " + NUID + "\n" 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_HOSTNAME, TCP_PORT))
s.send(INITIAL_MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print "received data:", data