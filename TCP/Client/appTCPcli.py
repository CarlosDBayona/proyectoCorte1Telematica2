import socket
import os
import time
import sys

TCP_IP = sys.argv[2]
FILE_PORT = int(sys.argv[3])
DATA_PORT = int(sys.argv[3])+1
buf = 1024
directory = sys.argv[1]
while True:
    info = input("TCP Client"+"\n")
    if info == "q":
        break
    if info == "l":
        print(os.listdir(directory))
    if info[0] == "e":
        start = time.time()
        try:
            file_name =info[1:]
            file_name = file_name.replace(" ", "")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((TCP_IP, FILE_PORT))
            sock.send(bytearray(file_name,"utf-8"))
            sock.close()
            print ("Sending %s ..." % file_name)
            f = open(directory+file_name, "rb")
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