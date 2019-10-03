# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time, random

host = sys.argv[1]
textport = sys.argv[2]
n = 10

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

while n is not 0:
    print ("Generating a random number to send...")
    data = random.randint(0, 1000) # Generates a random number from 0 to 1000
    print ("Sending " + str(data))
    s.sendto(str(data).encode('utf-8'), server_address)
    n -= 1;

s.shutdown(1)
