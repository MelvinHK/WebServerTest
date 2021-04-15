from socket import *

serverPort = 80
serverSocket = socket(AF_INET, SOCK_STREAM) # Make TCP server socket
serverSocket.bind(('', serverPort)) # Bind address and port number to the socket
serverSocket.listen(1) # Listen to TCP requests from client, parameter is max number of connections
print('Ready to serve...')
while True:
    connectionSocket, addr = serverSocket.accept() # Create new socket dedicated to the client, TCP connection is now established
    try:
        message = connectionSocket.recv(1024) # Get request header (packet data) from client
        print(message) # Print the request header
        filename = message.split()[1] # Extract /simpleWeb.html from req header
        f = open(filename[1:]) # Open the file
        outputdata = f.read()
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode()) # Send success status response to client
        for i in range(0, len(outputdata)): # Display webpage by sending the file character by character
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError: # If file name not found:
        connectionSocket.send('404 NOT FOUND\r\n\r\n'.encode()) # Send fail status
        connectionSocket.close()
serverSocket.close()
sys.exit()


