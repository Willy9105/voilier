import socket
class VoilierClient:

    def __init__(self):
        self.idTrame=0
        self.ipserveur=""
        self.port=0
        self.orientationSafran=0
        self.orientationGv=0
        self.oGite=0
        self.lat=0
        self.lon=0
        self.vVent=0
        self.dVent=0
        self.tailleTrame=0


    def intcom(self,ip,port):
        self.ipserveur=ip
        self.port=port
        self.sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def txrx(self):
        trame=bytearray([self.idTrame,2,self.orientationSafran,self.orientationGv]);
        self.sock.sendto(trame,(self.ipserveur,self.port))
        data,addr=self.sock.recvfrom(1024)

        b3=float (ord(data[5])<<24)
        b2=b3+(ord(data[6])<<16)
        b1=b2+(ord(data[7])<<8)
        b0=b1+(ord(data[8]))

        if ord(data[5]) > 127:
            b0= (~b0) &0xFFFFFFFF
            b0 = (b0+1)*-1
        lat = float(b0)/1000000

        c3=(ord(data[9])<<24)
        c2=c3+(ord(data[10])<<16)
        c1=c2+(ord(data[11])<<8)
        c0=c1+(ord(data[12]))
       
        if ord(data[9]) > 127:
            c0=(~c0)&0xFFFFFFFF
            c0=(c0+1)*-1
        lon= float(c0)/1000000

        self.idTrame+=1
        self.tailleTrame=ord(data[1])
        self.lat=lat
        self.lon=lon
        self.vVent=ord(data[2])
        self.dVent=ord(data[3])
        self.oGite=ord(data[4])

monVoilierClient=VoilierClient()
monVoilierClient.intcom("127.0.0.1",5005)
monVoilierClient.orientationSafran=30
monVoilierClient.idTrame=22
monVoilierClient.orientationGv=90
monVoilierClient.txrx()
print "taille= ",monVoilierClient.tailleTrame
print "Vitesse Vent= ",monVoilierClient.vVent
print "Direction Vent= ",monVoilierClient.dVent
print "Latitude= ",monVoilierClient.lat
print "Longitude= ",monVoilierClient.lon
print "Orientation Gite= ",monVoilierClient.oGite


    

    
