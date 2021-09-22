import socket

masg="hello udp server"

bytes=str.encode(masg)
servaddport=('127.0.0.1',20001)
buff=1024
ucs=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
ucs.sendto(bytes,servaddport)
msgfserv = ucs.recvfrom(buff)
msg="message from server{}".format(msgfserv[0])
print(msg)