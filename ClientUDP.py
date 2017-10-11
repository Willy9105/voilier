#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
ip="127.0.0.1"                    #Adresse IP du serveur
port= 5005
idTrame=22
tailleTrame=4
orientationSafran=30
orientationGv=90

trame=bytearray([idTrame,tailleTrame,orientationSafran,orientationGv])                    #bytearray -> 1 octet

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.sendto(trame,(ip,port))

data,addr=sock.recvfrom(1024)

b3=float (ord(data[5])<<24)
b2=b3+(ord(data[6])<<16)
b1=b2+(ord(data[7])<<8)
b0=b1+(ord(data[8]))
lat=(b0/10000)

c3=float (ord(data[9])<<24)
c2=c3+(ord(data[10])<<16)
c1=c2+(ord(data[11])<<8)
c0=c1+(ord(data[12]))
lon=(c0/10000)

print 'ID de trame :', ord(data[0])
print 'Taille de la trame :', ord(data[1])
print 'Vitesse du vent :', ord(data[2])
print 'Direction du vent :',ord(data[3]),'°'
print 'Gite :',ord(data[4]),'°'
print 'latitude :',lat
print 'longitude :',lon

