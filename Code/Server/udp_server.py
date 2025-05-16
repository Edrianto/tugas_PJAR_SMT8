import socket
import os
import time

BUFFER_SIZE = 32
BUFFER_FILENAME = 1024
SERVER_IP = 'localhost'
SERVER_PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Starting server on port ',SERVER_PORT)

sock.bind((SERVER_IP, SERVER_PORT))     

while True:
    print('Waiting to receive message')
    file_name, client_addr = sock.recvfrom(BUFFER_FILENAME)
    print(client_addr,' connected')
    start = time.time()

    file_name = file_name.decode()
    file_name = os.path.basename(file_name)

    fd = open(file_name, 'rb')
    buf = fd.read(BUFFER_SIZE)

    print('Sending Data')

    while(buf):
        sock.sendto(buf, client_addr)
        buf = fd.read(BUFFER_SIZE)
    
    fd.close()
    
    end = time.time()
    print(f"Time taken to upload: {end - start} sec")
    print(file_name," uploaded")
