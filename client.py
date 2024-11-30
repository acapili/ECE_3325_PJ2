#will connect to the server on TCP port 23456

#prompt for keyboard input.

#“QUIT”, the client program will close the TCP connection
# to the server and it will then exit normally through the
# bottom of the program (no break or immediate quit).

#“TIME” in the client program, the command will be sent to the server
# and the server will return its system time, then the client will display
# the servers system time.

from socket import *

serverName = '127.0.0.1'
serverPort = 23456



clientSocket = socket(AF_INET, SOCK_STREAM)#create TCP socket for server
clientSocket.settimeout(10) #gives the program time to connect
clientSocket.connect((serverName, serverPort))

while True:
    sentence = input('Input TIME or QUIT cmd: ')

    if sentence.lower() == 'quit':#if quit break loop
        break
    
    # Send the message
    clientSocket.send(sentence.encode())#no need to attach server name, port
    
    # Receive the modified message
    modifiedSentence = clientSocket.recv(1024).decode()
    print('From Server:', modifiedSentence)

print('Closing connection to ')
clientSocket.close()