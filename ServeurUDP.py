#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
IPserv="192.168.0.232"
Port=5005

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((IPserv,Port))

while True:
	data,addr=sock.recvfrom(1024)

	print data

