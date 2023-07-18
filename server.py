import socket
import threading

def handle_client(client_socket):
    # Receive and print messages from the client
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print("Received message from client:", data)
        
        # Send a response back to the client
        response = input("Enter your response: ")
        client_socket.send(response.encode())
    
    # Close the connection
    client_socket.close()

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name and specify a port for communication
host = socket.gethostname()
port = 12345

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)
print("Waiting for incoming connections...")

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print("Connected to:", client_address)

    # Create a new thread to handle the client connection
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()