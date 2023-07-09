import os
import time
from decouple import config

# Get the path to the directory we are in
base_dir = os.path.dirname(os.path.abspath(__file__))
# Get the configuration setting for re_read_on_query
reread_on_query = config("REREAD_ON_QUERY", cast=bool)

# Get the path from the configuration file
file = config("linuxpath")
#Get the configuration size from environment
payload_size = config("max_payload_size")
max_payload_size=int(payload_size)
config_file_path = os.path.join(base_dir, file)



def load_config():
    # Load the configuration file and extract the file path
    with open(config_file_path, 'r') as config_file:
        # Add your logic here to extract the relevant data from the configuration file
        print("Configuration file loaded")
        return True
    return None

def handle_client(connection, address):
    # Receive the string input from the client
    data = connection.recv(max_payload_size)
    received_string = data.decode().strip('\x00')
    # Print the search string received from the client  on the server
    print("Received search string from the client:", received_string)
    # Get the current time
    Search_Message = "Search in Progress"

    # Send the current time to the client
    connection.send(Search_Message.encode('ascii'))





    # Check the payload size
    if len(received_string) > max_payload_size:
        response = "PAYLOAD TOO LARGE\n"
    else:
        # Search for the string in the file
        exists, time_taken = search_string_in_file(received_string, config_file_path)

        # Respond to the client based on the search result
        if exists:
            response = "STRING EXISTS\n"
        else:
            response = "STRING NOT FOUND\n"
        response += "Time taken: {} milliseconds\n".format(time_taken)
        print(response)

    # Send the response to the client
    connection.send(response.encode('ascii'))

    # Close the connection
    connection.close()
    print("End of search")

import time

def search_string_in_file(search_string, file_path):
    # Starting the search
    print("Search started")
    start_time = time.time()
        
    
    if reread_on_query:
        # Record the start time
        print("reread is on ")
        
        # Read the contents of the file on every search query
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip() == search_string:
                    # Record the end time
                    end_time = time.time()
                    time_taken = (end_time - start_time) * 1000  # Convert to milliseconds
                    print("Time taken to search:", time_taken, "milliseconds")
                    return True, time_taken

        # If the search string was not found
        end_time = time.time()
        time_taken = (end_time - start_time) * 1000  # Convert to milliseconds
        print("Time taken to search:", time_taken, "milliseconds")
        return False, time_taken
    
    else:
        # Read the file contents only once, on load
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip() == search_string:
                    # Record the end time
                    end_time = time.time()
                    time_taken = (end_time - start_time) * 1000  # Convert to milliseconds
                    print("Time taken to search:", time_taken, "milliseconds")
                    return True, time_taken

    # If the search string was not found
    return False, 0
