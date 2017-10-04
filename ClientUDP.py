import socket

IP="192.168.0.232"              #Adresse IP du serveur
Port= 5005

sock= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     #AF_INET:Internet ,SOCK.DGRAM (pour UDP), SOCK.STREAM (pour TCP)
sock.sendto("Willy",(IP,Port))
