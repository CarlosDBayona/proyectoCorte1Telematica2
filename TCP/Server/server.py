import socket
import os
import time
import sys

TCP_IP = "127.0.0.1"
FILE_PORT = 5005
DATA_PORT = 5006
buf = 1024
file_name = sys.argv[1]

start = time.time()
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, FILE_PORT))
    sock.send(bytearray( file_name,"utf-8"))
    sock.close()
    print ("Sending %s ..." % file_name)
    f = open(file_name, "rb")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, DATA_PORT))
    data = f.read(buf)
    while(data):
        if(sock.send(data)):
            data = f.read(buf)
            time.sleep(0.02) # Give receiver a bit time to save

finally:
    sock.close()
    f.close()
stop = time.time()
print(stop-start)