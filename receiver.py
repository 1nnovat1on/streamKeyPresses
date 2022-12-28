import socket
import json

# Set the IP address and port to listen on
receiver_ip = ''
receiver_port = ''       

# Create a socket to receive data
receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and port
receiver.bind((receiver_ip, receiver_port))

# Start listening for incoming connections
receiver.listen(1)

while True:
    # Accept an incoming connection
    connection, addr = receiver.accept()

    # Read the incoming data
    data_json = connection.recv(1024).decode()

    # Convert the data to a dictionary
    data = json.loads(data_json)

    # Extract the coordinates and keypress from the dictionary
    x = data['x']
    y = data['y']
    key = data['key']

    # Process the coordinates and keypress as needed
    print(f'Received coordinates: ({x}, {y})')
    print(f'Received keypress: {key}')

    # Close the connection
    connection.close()

# Close the socket
receiver.close()
