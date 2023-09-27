[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Bp585G7b)

# **Documentation for the Socket Client Code**
This document provides an explanation of the Python codes that implements a socket client and server seperately. The client connects to a server and sends a number for calculation. The server then performs a calculation on the number and sends the result back to the client.

## **client.py explanation**

### **1. Importing Required Modules**

```python
import socket
import random
```
The code begins by importing the necessary Python modules. socket is used for socket programming, and random is used for selecting a random server port from a list.

### **2. Creating a Socket**

```python
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print(f"socket creation failed with error {err}")
```
A socket object client is created with the AF_INET address family (IPv4) and SOCK_STREAM socket type (TCP). If the socket creation fails, it will print an error message.

### **3. Server Configuration**

```python
serv_ports = [9001, 9002, 9003]
serv_ip = '127.0.0.1'
```
The code defines a list of server ports (serv_ports) and sets the server's IP address (serv_ip) to '127.0.0.1', which is the loopback address (localhost).

### **4. Client Input and Main Loop**

```python
while True:
    client_input = input("Enter number to calculate: (or write exit to terminate): ")

    if client_input.lower() == "exit":
        break
```
The code enters a loop that allows the user to input numbers to be sent to the server for calculation. The loop continues until the user enters "exit," at which point the program terminates.

### **5. Random Server Port Selection**

```python
serv_port = random.choice(serv_ports)
```
A random server port is selected from the list of serv_ports.

### **6. Connecting to the Server**

```python
try:
    client.connect((serv_ip, serv_port))
    print(f"connected to Server {serv_ip}:{serv_port}")
```
The client attempts to connect to the server using the selected server IP address and port. If the connection is successful, it prints a message indicating the connection.

### **7. Sending Data to the Server**

```python
client.send(client_input.encode('utf-8'))
```
The client sends the user's input (a number to be calculated) to the server after encoding it as UTF-8.

### **8. Receiving and Displaying Server Response**

```python
response = client.recv(1024).decode('utf-8')
print(f"Received from server: {response}")
```
The client receives a response from the server (the result of the calculation) and prints it to the console after decoding it from UTF-8.

### **9. Handling Connection Errors**

```python
except socket.error as err:
    print(f"Failed to connect to Server {serv_ip}:{serv_port} with error {err}")

```

If there is an error in connecting to the server, an error message is printed.

### **10. Closing the Socket**

```python
finally:
    client.close()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

In the finally block, the client socket is closed, and a new socket is created for the next iteration of the loop. This ensures that the client can attempt to connect to the server again.

### **11. Closing the Client Socket**

```python
client.close()
```

Finally, after the loop exits, the client socket is closed to release any resources.