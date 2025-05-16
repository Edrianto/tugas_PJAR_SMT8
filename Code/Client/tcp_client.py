import socket
import os
import time

BUFFER_SIZE = 32
HOST = 'localhost'
PORT = 12345

print("Enter the corresponding number to download book:")
print("1. Atlas Shrugged by Ayn Rand")
print("2. Don Quixote by Miguel de Cervantes")
print("3. Shogun by James Clavell")
print("4. The Stand by Stephen King")
print("5. War and Peace by Leo Tolstoy")

file_number = int(input())

if(file_number == 1):
    file_name = "Atlas Shrugged.txt"
elif(file_number == 2):
    file_name = "Don Quixote.txt"
elif(file_number == 3):
    file_name = "Shogun.txt"
elif(file_number == 4):
    file_name = "The Stand.txt"
elif(file_number == 5):
    file_name = "War and Peace.txt"

file = file_name.split('.')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print('Connecting to ',HOST)
    sock.connect((HOST, PORT))
    start = time.time()
    print('Connected')
    sock.send(f"{file_name}".encode())
    
    file_name = file[0] + "+Protocol=TCP" + "+" + str(os.getpid()) + "." + file[1]

    with open(file_name, 'wb') as f:
        print('Receiving Data')
        while True:
            byte = sock.recv(BUFFER_SIZE)

            if not byte:
                break

            f.write(byte)
    
finally:
    sock.close()
    end = time.time()      
    print(f"Time taken to download: {end - start} sec")

    file_stat = os.stat(file_name)
    file_size = file_stat.st_size

    throughput = round((file_size*0.001)/(end - start), 3)
    print("Downloaded ",file_name)
    print("Throughput: ",throughput,"kB/s")
    
