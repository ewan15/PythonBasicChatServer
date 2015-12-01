from socket import *
import threading
import sys
if sys.version_info >= (3,0):
    import _thread
else:
    import thread


from threading import Thread

def CheckRecv():
    while True:
        try:
            dataRecv = clientsocket.recv(1024)
            dataRecv = dataRecv.decode()
            loc = dataRecv.index(']')
            user = dataRecv[1:loc]

            if username != user:
                print ("{}".format(dataRecv))
                print ("\n>>")
        except ValueError:
            print ("ERROR")
            exit()
def InputSys():
    while True:
        if sys.version_info >= (3,0):
            data = input(">> ")
        else:
            data = raw_input(">> ")
        if data != "":
            if data == "/help":
                print ("Use: /ext to exit the server\n")
            if data == "/ext":
                data = "[" + username + "]" + " Says: " + data
                data = data.encode()
                clientsocket.send(data)
                sys.exit()
            else:
                data = "[" + username + "]" + " Says: " + data
                data = data.encode()
                clientsocket.send(data)

if __name__ == '__main__':
    print ("\nTo exit the terminal please type '\ext'")
    if sys.version_info >= (3,0):
        username = input("Please enter your username: ")
    else:
        username = raw_input("Please enter your username: ")
    host = '192.168.10.61'
    port = 55567
    buf = 1024

    addr = (host, port)

    clientsocket = socket(AF_INET, SOCK_STREAM)

    clientsocket.connect(addr)
    data = clientsocket.recv(1024)
    print(data.decode())
    if sys.version_info >= (3,0):
        _thread.start_new_thread(CheckRecv, ())
        InputSys()
    else:
        thread.start_new_thread(CheckRecv, ())
        InputSys()
    print("Threads have not been started")
