#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
ip="127.0.0.1"
port=5005
idTrame=35
tailleTrame=5
vVent=42
dVent=57
oGite=77


sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((ip,port))



while True:
	data,addr=sock.recvfrom(1024)
	trame_reponse=bytearray([idTrame,tailleTrame,vVent,dVent,oGite])
	sock.sendto(trame_reponse,(addr[0],addr[1]))
	
	print 'ID de trame :', ord(data[0])
	print 'Taille de la trame :', ord(data[1])
	print 'Orientation safran :', ord(data[2]),'°'
	print 'Orientation de la GV :', ord(data[3]),'°'



