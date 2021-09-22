import socket
localIP = '127.0.0.1'
localport = 20001

bufferSize = 1024

msgFromServer = "Hello UPD Client"

bytesToSend = str.encode(msgFromServer)

UDPSERVERSOCKET = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) #1

UDPSERVERSOCKET.bind((localIP, localport))  #2

print("UDP server up and listening....")

while True:
    bytesAddressPair = UDPSERVERSOCKET.recvfrom(bufferSize) # 3
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientmsg = "Message from client{}".format(message)
    ClientIP = "Client IP address:{}".format(address)
    print(clientmsg)
    print(ClientIP)
    UDPSERVERSOCKET.sendto(bytesToSend, address) # 4
