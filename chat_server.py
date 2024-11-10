import socket  # Import socket module for network communication
import threading  # Import threading module for handling multiple clients

def start_server(host='127.0.0.1', port=8080):
    # Initialize a TCP socket for the server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))  # Bind the server to the specified host and port
    server.listen()  # Start listening for incoming connections
    print(f'Server running on {host}:{port}')
    
    clients = []  # List to keep track of connected clients

    # Function to broadcast messages to all clients except the sender
    def broadcast(message, sender):
        for client in clients:
            if client != sender:  # Avoid sending the message to the sender
                try:
                    client.send(message)  # Send message to client
                except:
                    clients.remove(client)  # Remove client if sending fails

    # Function to handle communication with an individual client
    def handle_client(client):
        while True:
            try:
                message = client.recv(1024)  # Receive message from client
                if message:
                    broadcast(message, client)  # Broadcast message to other clients
                else:
                    break  # Exit if no message is received
            except:
                break  # Exit on exception
        clients.remove(client)  # Remove client when disconnected
        client.close()  # Close the client's connection

    # Main loop to accept incoming client connections
    while True:
        client, _ = server.accept()  # Accept new client connection
        clients.append(client)  # Add client to list
        # Start a new thread to handle this client
        threading.Thread(target=handle_client, args=(client,)).start()

if __name__ == '__main__':
    start_server()  # Run the server
