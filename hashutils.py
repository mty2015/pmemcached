import md5
import random
import string


def gen_hash_code(object):
    return int(md5.new(object).hexdigest(),16) 

class Hash:
    def __init__(self,cache_servers):
        self.cache_servers =  cache_servers[:]

    def remove(self,cache):
        self.cache_servers.remove(cache)

    def add(self,cache):
        self.cache_servers.append(cache)

    def get(key):
        pass

class BasicHash(Hash):
    def get(self,key):
        return self.cache_servers[gen_hash_code(object) % len(self.cache_servers)]
        

class ConsistentHash(Hash):
    def __init__(self,cache_servers,number_of_replicas=1):
        self.cicle = {}
        for cache in cache_servers:
            self.add(cache,number_of_replicas)

    def remove(self,cache):
        for i in range(number_of_replicas):
            self.cicle.remove(gen_hash_code(cache[0] + str(i)))

    def add(self,cache,number_of_replicas=1):
        for i in range(number_of_replicas):
            self.cicle[gen_hash_code(cache[0] + str(i))] = cache

    def get(self,key):
        hash_key = gen_hash_code(key)
        keys = self.cicle.keys()
        keys.sort()
        for cache_key in keys:
            if hash_key <= cache_key:
                return self.cicle[cache_key]
        else:
            return self.cicle[keys[0]]
            


if __name__ == '__main__':
    cache_servers = (('192.168.1.101',11211),('192.168.1.121',11211),('192.148.1.6',11211))
    consistent = ConsistentHash(cache_servers,5)
    print 'the cache server status--------------'
    keys = consistent.cicle.keys()
    keys.sort()
    for key in keys:
        print consistent.cicle[key] , " on ", key
    print 'test the random key -----------'
    for i in range(50):
        key = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(20))
        print key , ' on ' ,consistent.get(key)

