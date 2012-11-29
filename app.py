import socket


CR = '\x0d'
LF = '\x0a'


def getSocket(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,port))
    return s 

class StreamHandler:
    
    BUFFER_SIZE = 1024

    def __init__(self,socket):
        self.socket = socket

    def write(self,s):
        msg_len = len(s)
        total_len = 0
        while total_len < msg_len:
            sent = socket.send(s[total_len:])
            if sent == 0:
                raise IOError('socket is broken')
            total_len = total_len + sent
    
    def read(self,max_len=0):
        s = ''
        while True:
            readed = self.socket.recv(StreamHander.BUFFER_SIZE)
            if readed == '':
                raise IOError('socket is broken')
            s = s + readed
            if (max_len == 0 and s.endswith(CR + LF)) or (max_len > 0 and len(s) == max_len):
                return s

class SocketFactory:
    def __init__(self,ip_list)


class PMemachedClient:
    
    def __init__(self,ip_list):
       self.ip_list = ip_list;

    def get(key):
        

if __name__ == '__main__':
    main()
