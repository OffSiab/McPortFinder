#!/usr/bin/python3
import sys
import socket

class McPortFinder:

    def __init__(self, host, sPort, ePort):
        self.host = host
        self.sPort=sPort
        self.ePort=ePort
        
    def isOpen(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.host, port))
            return True
        except:
            return False
        
    def getPorts(self):
        self.openPorts=[]
        port=self.sPort
        while port<=self.ePort:
            print("Testing " + str(self.host) + ":" + str(port))
            if(self.isOpen(port)):
                print("Port is open : " + str(port) + " !")
                self.openPorts.append(port)
            port+=1
        return self.openPorts

if __name__ == '__main__':
    host=""
    sPort=20000
    ePort=40000
    sys.argv.pop(0)
    if len(sys.argv)>=1:
        host=sys.argv[0]
        if len(sys.argv)>=2:
            sPort=int(sys.argv[1])
        if len(sys.argv)>=3:
            ePort=int(sys.argv[2])
        McPF = McPortFinder(host, sPort, ePort)
        print(McPF.getPorts())
    else:
        print("Usage : python3 McPortFinder.py <host> (startPort) (endPort)")
        
