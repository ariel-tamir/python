import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('www.example.com', 80))
sock.sendall('GET http://www.example.com/ HTTP/1.0\r\n\r\n'.encode('utf-8'))
data = sock.recv(10000)
print('received "%s"' % data.decode('utf-8'))

sock.close()
