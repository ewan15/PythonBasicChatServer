from socket import *
import _thread
clients = set()


def RmV(clientsocket):
    clients.remove(clientsocket)
    print ("Removing client socket")
    #clientsocket.close()

def handler(clientsocket, clientaddr):
    print ("Accepted connection from: ", clientaddr)

    clients.add(clientsocket)
    connected = 1
    WelcomeStr = " _    _      _                            _        \n\
| |  | |    | |                          | |       \n\
| |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___  \n\
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \ \n\
\  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | \n\
 \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  \n"

    welcomeStr2 = " _____                          _____                          \n\
|  ___|                        /  ___|                         \n\
| |____      ____ _ _ __  ___  \ `--.  ___ _ ____   _____ _ __  \n\
|  __\ \ /\ / / _` | '_ \/ __|  `--. \/ _ \ '__\ \ / / _ \ '__| \n\
| |___\ V  V / (_| | | | \__ \ /\__/ /  __/ |   \ V /  __/ |    \n\
\____/ \_/\_/ \__,_|_| |_|___/ \____/ \___|_|    \_/ \___|_|   "

    WelcomeStr = WelcomeStr + welcomeStr2




    clientsocket.send(WelcomeStr.encode())
    while (connected == 1):
        try:
            data = clientsocket.recv(1024)
            print ("Data recvieved")
        except ValueError:
            clients.remove(clientsocket)
            print ("Removing client socket")
            RmV(clientsocket)
            clientsocket.close()

        if not data:
            break
        else:

            data = data.decode()
            print (data)
            msg = (data).encode()
            locExt = data.index(']')
            extCode = data[1:locExt]
            loc = data.index(']')
            user = data[1:loc]
            userTxt = data[data.index(': '):]
            userTxt = userTxt[2:]
            if (userTxt == "/ext"):
                RmV(clientsocket)
                connected = 0
            elif (userTxt.startswith("/kick")):
                  userTxt = userTxt[6:]
                  print("Removed: ", userTxt)
            for i in clients: #problem i believe is in here but i

                print ("The text is: " + userTxt)
                if (userTxt == "/ext"):
                    i.sendall(("["+ user + "] Has disconnected" ).encode())
                else:
                    try:
                        i.sendall(msg)  #dont know how to fix it
                    except:
                        print ("Cant send user data\nDisconnecting User")


    clientsocket.close()

if __name__ == "__main__":
    host = ''
    port = 55567
    buf = 1024

    addr = (host, port)

    serversocket = socket(AF_INET, SOCK_STREAM)

    serversocket.bind(addr)

    serversocket.listen(2)

    while 1:
        print ("Server is listening for connections\n")

        clientsocket, clientaddr = serversocket.accept()
        _thread.start_new_thread(handler, (clientsocket, clientaddr))
    serversocket.close()
