import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('localhost', 10000))
sock.sendall('REL'.encode('utf-8'))
data = sock.recv(16)
print('received "%s"' % data.decode('utf-8'))

sock.sendall("Alon".encode("utf-8"))
data2 = sock.recv(16)
print('received "%s"' % data2.decode('utf-8'))

sock.close()
