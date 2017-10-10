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

while True:
    data,addr=sock.recvfrom(1024)
    print 'ID de trame :', ord(data[0])
    print 'Taille de la trame :', ord(data[1])
    print 'Vitesse du vent :', ord(data[2])
    print 'Direction du vent :',ord(data[3]),'°'
    print 'Gite :',ord(data[4]),'°'

