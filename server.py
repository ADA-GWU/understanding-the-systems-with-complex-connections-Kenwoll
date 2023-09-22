import socket 
import sys

if len(sys.argv) != 2:
    print("Usage: python server.py <server number>. For further information check readme file")
    sys.exit(1)

try:
    serv_num = int(sys.argv[1])
except ValueError:
    print("Invalid argument. Please provide an integer.")
    sys.exit(1)

ip = "127.0.0.1"
port = 9000 + serv_num

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((ip, port))
serv.listen(5)
print(f"Server is listening on {ip}:{port}")

while True:
    client_sock, client_addr = serv.accept()
    print(f"Accepted connection from {client_addr}")

    try:
        data = client_sock.recv(1024).decode('utf-8')
    except socket.error as e:
        if e.errno == 10038:
            print("The client socket is closed")
        
    if not data:
        break
        
    print(f"Received from client: {data}")
        
    try:
        response = str(int(data) * 2)
    except ValueError:
        response = "Received data is not valid integer"
        
    client_sock.send(response.encode('utf-8'))

serv.close()