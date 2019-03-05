import socket
import time
import threading
import os
import sys

TCP_IP = "localhost"
location = str(sys.argv[2])
FILE_PORT = int(sys.argv[1])
DATA_PORT = int(sys.argv[1])+1
timeout = 3
buf = 1024
sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_f.bind((TCP_IP, FILE_PORT))
sock_f.listen(1)
sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_d.bind((TCP_IP, DATA_PORT))
sock_d.listen(1)
def readFile():
    while True:
        conn, addr = sock_f.accept()
        data = conn.recv(buf)
        if(data):
            if data:
                print("File name:", data)
                file_name_str = str(data)
                file_name_str = file_name_str[1:]
                file_name_str = file_name_str.replace("'", "")
            f = open(str(location)+str(file_name_str), 'wb')
            conn, addr = sock_d.accept()
            while True:
                data = conn.recv(buf)
                if not data:
                    break
                f.write(data)
            print("%s Finish!" % file_name_str)
            f.close()
        else:
            time.sleep(1)


thread1 = threading.Thread(target=readFile)
thread1.daemon = True
thread1.start()
while True:
    info = input("TCP Server"+"\n")
    if info == "q":
        break
    if info == "l":
        print(os.listdir('./db'))
