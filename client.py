import socket
import threading

def receive_messages(client_socket):
    # Receive and print messages from the server
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print("Received message from server:", data)

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the server machine name and port
server_host = socket.gethostname()
server_port = 12345

# Connect to the server
client_socket.connect((server_host, server_port))

# Start a new thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

# Send messages to the server
while True:
    message = input("Enter your message ('q' to quit): ")
    if message == 'q':
        break
    client_socket.send(message.encode())

# Close the connection
client_socket.close()

