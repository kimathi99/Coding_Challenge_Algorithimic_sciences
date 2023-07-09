import socket
import threading
import loading

import time

def start_server():
    # Load the configuration
    file_path = loading.load_config()

    if file_path is None:
        print("Error: Configuration file not found or path not specified")
        return

    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_socket.bind(('0.0.0.0', 44445))

    # Enable listening for incoming connections
    server_socket.listen()

    print("Server started. Listening for connections on port 44445")

    while True:
        # Accept a client connection
        connection, address = server_socket.accept()

        # Print the client's address
        print("Got a connection from %s" % str(address))

        # Get the current time
        currentTime = time.ctime(time.time()) + "\r\n"

        # Send the current time to the client
        connection.send(currentTime.encode('ascii'))



        # Start a new thread to handle the client
        client_thread = threading.Thread(
            target=loading.handle_client,
            args=(connection, address)
        )
        client_thread.start()

if __name__ == '__main__':
    # Set the search string
   

    # Start the server
    start_server()
