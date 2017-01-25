import socket
# writing a simple browser for accessing website
#sockets work at transport layer-low level layer

my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_socket.connect(('www.py4inf.com',80))

my_socket.send(b'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n ') #b-stands for data sent/received should in bytes


while True:
    data= my_socket.recv(512)
    if (len(data)<1):
        break
    print(data)
my_socket.close()