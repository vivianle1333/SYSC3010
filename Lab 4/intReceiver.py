# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time

textport = sys.argv[1]
n = 10
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ('localhost', port)
s.bind(server_address)

while n > 0:
    print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)
    buf, address = s.recvfrom(port)
    print("Random number received: " + buf.decode('utf-8'))
    n -= 1;

s.shutdown(1)
