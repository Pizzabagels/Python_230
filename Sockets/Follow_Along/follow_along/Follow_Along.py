import socket

socket.getaddrinfo('hasthelargehadroncolliderdestroyedtheworldyet.com', 'http')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
client.connect(('216.92.96.71', 80))
msg = "GET / HTTP/1.1\r\n"
msg += "Host: hasthelargehadroncolliderdestroyedtheworldyet.com\r\n\r\n"
msg = msg.encode('utf8')
print(msg)
client.sendall(msg)
response = client.recv(64)
print(response)
client.close()
