import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 10000))
sock.listen(1)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        request = connection.recv(16)
        print(request.decode('utf-8'))
        connection.sendall('yes'.encode('utf-8'))

        request2 = connection.recv(16)
        print(request2.decode('utf-8'))

        mashu= request + request2
        connection.sendall(mashu)

    finally:
        connection.close()
