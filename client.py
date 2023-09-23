import socket
import random

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print(f"socket creation failed with error {err}")

serv_ports = [9001, 9002, 9003]
serv_ip = '127.0.0.1'

while True:
    client_input = input("Enter number to calculate: (or write exit to terminate): ")

    if client_input.lower() == "exit":
        break

    serv_port = random.choice(serv_ports)

    try:
        client.connect((serv_ip, serv_port))
        print(f"connected to Server {serv_ip}:{serv_port}")

        client.send(client_input.encode('utf-8'))

        response = client.recv(1024).decode('utf-8')
        print(f"Received from server: {response}")
    
    except socket.error as err:
        print(f"Failed to connect to Server {serv_ip}:{serv_port} with error {err}")
    
    finally:
        client.close()
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Close the client socket
client.close() 