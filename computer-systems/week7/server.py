import socket

s=socket.socket()
port=12345
s.bind(('', port))
print("socket binded to %s" %(port))

s.listen(5)
print("Socket is listening")
while True:
    c, addr =s.accept()
    print("Got connection from", addr)

    c.send('Thanks for connection' .encode())
    c.close()
    break