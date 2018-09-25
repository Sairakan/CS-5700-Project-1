# -*- coding: utf-8 -*-
"""
Authors: Jason Teng
2018-9-24

This file contains the server code for CS 5700 Project 1
"""

import socket, select

# basic validation of start and end of message
def isValid(message):
    return message.startswith('cs5700fall2018 ') and message.endswith('\n')
    
# returns numeric result of STATUS message
def solve(message):
    ops = message.split()
    if len(ops) < 5:
        assert 'invalid message'
        exit()
    firstnum = int(ops[2])
    operator = ops[3]
    secondnum = int(ops[4])
    
    if operator == '+':
        return firstnum + secondnum
    if operator == '-':
        return firstnum - secondnum
    if operator == '*':
        return firstnum * secondnum
    if operator == '/':
        return firstnum // secondnum
    
    
# message handler
def handleMessage(message, s):
    if not isValid(message):
        assert 'invalid message'
        exit()
    elif message.find('STATUS') >= 0:
        result = solve(message)
        print(result)
        s.send("cs5700fall2018 " + str(result) + "\n")
        return
    elif message.find('BYE') >= 0:
        secret_flag = message.split()[1]
        print(secret_flag)
        s.close()
        exit()
        

# Connection Setup
TCP_HOSTNAME = "cs5700f18.ccs.neu.edu"
TCP_PORT = 27993

BUFFER_SIZE = 1024
NUID = "001876580"

INITIAL_MESSAGE = "cs5700fall2018 HELLO " + NUID + "\n" 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_HOSTNAME, TCP_PORT))
s.send(INITIAL_MESSAGE)

# Event loop
while True:
    try:
        readable, writable, errored = select.select([s,], [], [], 3)
    except select.error:
        s.close()
        exit()
    if len(readable) > 0:
        message = s.recv(2048)
        print(message)
        handleMessage(message, s)
    else:
        print 'timeout'
