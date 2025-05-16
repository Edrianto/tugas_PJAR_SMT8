import socket
import os
import time

BUFFER_SIZE = 32
BUFFER_FILENAME = 1024
SERVER_IP = 'localhost'
SERVER_PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Starting server on port ',SERVER_PORT)

sock.bind((SERVER_IP, SERVER_PORT))

sock.listen(1)                                              

while True:
    print('Waiting for connection')
    connection, client_addr = sock.accept()

    try:
        start = time.time()
        print(client_addr,' connected')
        file_name = connection.recv(BUFFER_FILENAME).decode()
        file_name = os.path.basename(file_name)
       
        fd = open(file_name, 'rb')
        buf = fd.read(BUFFER_SIZE)

        print('Sending Data')

        while(buf): 
            connection.send(buf)
            buf = fd.read(BUFFER_SIZE)
        
        fd.close()

        end = time.time()
        print(f"Time taken to upload: {end - start} sec")
        print(file_name," uploaded")

    finally:
        connection.close()
        
