# Source: https://pymotw.com/2/socket/udp.html
import json
import socket, sys, time, random

host = sys.argv[1]
textport = sys.argv[2]
n = 10
a = 0
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

while n is not 0:
    # Convert dict to json
    if n is not 10:
        x['age'] = x['age'] + 1
    y = json.dumps(x)
    print ("Sending " + y)
    s.sendto(y.encode('utf-8'), server_address)
    n -= 1

s.shutdown(1)
