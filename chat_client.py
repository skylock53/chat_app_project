import socket  # Import socket module for network communication
import threading  # Import threading module for handling message reception

def start_client(host='127.0.0.1', port=8080):
    # Initialize a TCP socket for the client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))  # Connect to the server at specified host and port
    print(f'Connected to server at {host}:{port}')

    # Function to continuously receive messages from the server
    def receive_messages():
        while True:
            try:
                # Receive messages from server and decode them
                print(client.recv(1024).decode('utf-8'))
            except:
                break  # Exit loop if an error occurs

    # Start a separate thread for receiving messages from the server
    threading.Thread(target=receive_messages).start()

    # Main loop to send user input as messages to the server
    while True:
        message = input()  # Get message from user
        if message.lower() == 'exit':  # Check if user wants to exit
            break  # Exit loop
        client.send(message.encode('utf-8'))  # Send message to server

    client.close()  # Close the client connection when done

if __name__ == '__main__':
    start_client()  # Run the client
