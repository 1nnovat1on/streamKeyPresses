import socket
import json
import pyautogui

# Create a socket to send data over
sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the IP address and port of the receiver
receiver_ip = '' #insert ip here
receiver_port = 138

# Connect to the receiver
sender.connect((receiver_ip, receiver_port))

# Create a dictionary to store the data
data = {'x': 10, 'y': 20, 'key': 'a'}

# Convert the data to a JSON string
data_json = json.dumps(data)

# Send the data to the receiver
sender.send(data_json.encode())

# Close the socket
sender.close()
