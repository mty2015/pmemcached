# -*- coding:utf-8 -*-
from streambuffer import StreamHandlerFactory
from protocol import *

class SocketFactory:
    def __init__(self,ip_list):
        self.consistent        

class StoreException(Exception):
    def __init__(self,msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

class PMemcachedClient:
    
    def __init__(self,cache_servers_conf):
        self.streamHandlerFactory = StreamHandlerFactory(cache_servers_conf)

    def get(self,key):
        handler = self.streamHandlerFactory.getStreamHandler(key)
        handler.write_line('get ' + key)
        meta = handler.read_line()
        print meta
        data = handler.read(12)
        print data
    
    def add(self,key,value,tracking_data=0,exptime=0,asyn=False):
        handler = self.streamHandlerFactory.getStreamHandler(key)
        handler.write_line(assemble_store_command("add",key,value,tracking_data,exptime,asyn))
        handler.write_line(value)
        if asyn: #asyn means don't required to read feedback
            return
        return parse_store_reply(handler.read_line())

if __name__ == '__main__':
    cache_servers = (('184.82.204.80',11211),)
    client = PMemcachedClient(cache_servers)
    print client.add('tony3',u'李'.encode('gbk'))
