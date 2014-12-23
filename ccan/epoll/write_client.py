
# http://pymotw.com/2/socket/tcp.html
import socket
import sys

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening

server_address = ('localhost', 100000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:

    # Send data
    message = 'This is the message. It will be repeated\n'
    print >>sys.stderr, 'sending "%s"' % message

    for _ in range(100000):
        sock.sendall(message)

    sys.exit(1)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
