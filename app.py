import socket
def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('localhost',11211))
    s.send('get abc\x0d\x0a')
    data = s.recv(1024)
    print data



if __name__ == '__main__':
    main()
