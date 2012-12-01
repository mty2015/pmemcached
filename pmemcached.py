import socket
from hashutils import ConsistentHash 


CR = '\x0d'
LF = '\x0a'


def getSocket(address):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(address)
    return s 

class StreamHandler:
    
    BUFFER_SIZE = 1024

    def __init__(self,socket):
        self.socket = socket
        self.read_buffer = ''

    def write(self,s):
        msg_len = len(s)
        total_len = 0
        while total_len < msg_len:
            sent = self.socket.send(s[total_len:])
            if sent == 0:
                raise IOError('socket is broken')
            total_len = total_len + sent
    
    def read(self,size):
        while True:
            if len(self.read_buffer) >= size:
                data = self.read_buffer[:size]
                self.read_buffer = self.read_buffer[size:]
                return data
            readed = self.socket.recv(size - len(self.read_buffer))
            if readed == '':
                raise IOError('socket is broken')
            self.read_buffer = self.read_buffer + readed


    def read_line(self):
        while True:
            sep_index = self.read_buffer.find(CR + LF)
            if sep_index != -1:
                line =  self.read_buffer[:sep_index]
                self.read_buffer = self.read_buffer[sep_index + 2:]
                return line
            readed = self.socket.recv(StreamHandler.BUFFER_SIZE)
            if readed == '':
                raise IOError('socket is broken')
            self.read_buffer = self.read_buffer + readed
            
            



class SocketFactory:
    def __init__(self,ip_list):
        self.consistent        


class PMemcachedClient:
    
    def __init__(self,cache_servers_conf):
        self.cache_servers = ConsistentHash(cache_servers_conf,5)


    def get(self,key):
        handler = StreamHandler(getSocket(self.cache_servers.get(key)))
        handler.write('get ' + key + CR + LF)
        meta = handler.read_line()
        print meta
        data = handler.read(12)
        print data

        

if __name__ == '__main__':
    cache_servers = (('localhost',11211),)
    client = PMemcachedClient(cache_servers)
    print client.get('abc')
