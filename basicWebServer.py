from socket import *

serverPort = 80
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a server socket
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        print(message)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        # Send
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send('404 NOT FOUND\r\n\r\n'.encode())
        connectionSocket.close()
serverSocket.close()
sys.exit()


