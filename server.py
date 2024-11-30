#listen on TCP port 23456 for TCP connections.


#determine if it is a valid command, 
#and return the results back to the sender.

from socket import *
from datetime import datetime

serverPort = 23456
serverSocket = socket(AF_INET, SOCK_STREAM)#create TCP welcoming socket
serverSocket.bind(('', serverPort))
serverSocket.listen(1)#server begins listening for incoming TCP requests

print("Server is ready to receive")

try:#closes the server from Ctrl + C

    while True:
        connectionSocket, addr = serverSocket.accept()#Waits on accept() for incoming requests
        print(f"Connection from {addr}")

        while True:
            sentance = connectionSocket.recv(1024).decode()#read bytes from socket
            
            # Case statement to handle different commands
            match sentance.upper():
                case "TIME":#IME cmd
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    response = f"Current server time is: {current_time}"
                    connectionSocket.send(response.encode())
                
                case "QUIT":#QUIT cmd
                    response = "Closing connection"
                    connectionSocket.send(response.encode())
                    break
                
                case _:#default for an invalid command
                    response = "Invalid command"
                    connectionSocket.send(response.encode())
            
            print(f"Sent: {response}")
    
        connectionSocket.close()#closes connection and goes back to waiting
        print("Connection closed")

except KeyboardInterrupt:
    print("\nServer is shutting down")

finally:
    # Ensure the socket is closed
    serverSocket.close()