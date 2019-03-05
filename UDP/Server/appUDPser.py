import socket
import time
import sys
import os
import threading
import select

UDP_IP = "localhost"
IN_PORT = int(sys.argv[1])
location = str(sys.argv[2])
timeout = 3


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, IN_PORT))

def readFile():
    while True:
        data, addr = sock.recvfrom(1024)
        if data:
            if data:
                print ("File name:", data, "From", addr)
                file_name_str=str(data)
                file_name_str = file_name_str[1:]
                file_name_str = file_name_str.replace("'","")
                f = open(location+str(file_name_str), 'wb')

                while True:
                    ready = select.select([sock], [], [], timeout)
                    if ready[0]:
                        recvdata, addr = sock.recvfrom(1024)
                        f.write(bytearray(recvdata))
                    else:
                        print ("%s Finish!" % file_name_str)
                        f.close()
                        break
        else:
            time.sleep(1)
thread1 = threading.Thread(target=readFile)
thread1.daemon=True
thread1.start()
while True:
    info = input("UDP Server"+"\n" )
    if info == "q":
        break
    if info == "l":
        print(os.listdir('./db'))