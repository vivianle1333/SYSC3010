# Source: https://pymotw.com/2/socket/udp.html
import json
import socket, sys, time

textport = sys.argv[1]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ('localhost', port)
s.bind(server_address)

while True:
    print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)
    buf, address = s.recvfrom(port)
    print("Received: " + buf.decode('utf-8'))
    y = json.loads(buf.decode('utf-8'))
    print("Converted to Python Dictionary: " + str(y))
    print("\n\n")

s.shutdown(1)
