# memcached客户端（python）

## 快速使用
```python
import pmemcached

cache_servers = (('192.168.1.101',11211),('192.168.1.121',11211),('192.148.1.6',11211)) #缓存服务器列表
client = PMemcachedClient(cache_servers) #创建客户端对象
client.add('id001','54844') #往缓存服务器存值 
print client.get('id001') #往缓存服务器取值
```

## 支持特性
* 支持多缓存服务器，并初始化时设置权重大小，对于内存大的服务器可以更多利用
* 支持一致性hash调度，在动态改变服务器数量时更稳定

## 下次改进
* NIO 支持
* socket连接池支持
