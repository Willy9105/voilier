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
lat=12.3456
lon=89.1234

lon1=int (lon*10000)
c3=(lon1>>24)
c2=(lon1>>16)&0xFF
c1=(lon1>>8)&0xFF
c0=lon1&0xFF

lat1=int (lat*10000)
b3=(lat1>>24)
b2=(lat1>>16)&0xFF
b1=(lat1>>8)&0xFF
b0=lat1&0xFF


sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((ip,port))



while True:
	data,addr=sock.recvfrom(1024)
	trame_reponse=bytearray([idTrame,tailleTrame,vVent,dVent,oGite,b3,b2,b1,b0,c3,c2,c1,c0])
	sock.sendto(trame_reponse,(addr[0],addr[1]))
	
	print 'ID de trame :', ord(data[0])
	print 'Taille de la trame :', ord(data[1])
	print 'Orientation safran :', ord(data[2]),'°'
	print 'Orientation de la GV :', ord(data[3]),'°'



