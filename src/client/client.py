import socket

def send_request(host, port, search_string):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Set the timeout for receiving responses
        client_socket.settimeout(5)

        # Connect to the server
        client_socket.connect((host, port))

        # Send the search string as the request
        client_socket.sendall(search_string.encode())

        # Receive and print the response
        while True:
            try:
                response = client_socket.recv(1024).decode()
                if not response:
                    break
                print("Response:", response)
            except socket.timeout:
                # Timeout occurred
                print("Response timeout occurred.")
                break

    finally:
        # Close the socket
        client_socket.close()

if __name__ == '__main__':
    # Server address and port
    host = 'localhost'
    port = 44445

    # Request parameters
    search_string = "11;0;1;16;0;12;4;0;"

    # Send the request
    send_request(host, port, search_string)
