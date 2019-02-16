import socket
import time
import sys
import os

UDP_IP = sys.argv[2]
UDP_PORT = int(sys.argv[3])
buf = 1024
file_name = sys.argv[1]

while True :
    info = input("UDP Client"+"\n" )
    if info == "q":
        break
    if info == "l":
        print(os.system('dir'))
    if info == "e":
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytearray( file_name, "utf-8"), (UDP_IP, UDP_PORT))
        print ("Sending %s ..." % file_name)
        start = time.time()
        f = open(file_name, "rb")
        data = f.read(buf)
        while(data):
            if(sock.sendto(data, (UDP_IP, UDP_PORT))):
                data = f.read(buf)
                time.sleep(0.02) # Give receiver a bit time to save

        sock.close()
        f.close()
        stop = time.time()
        print(stop-start)