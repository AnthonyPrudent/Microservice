# Microservice A - Python list scrambler

# To request data from the microservice, use ZeroMQ to send a string tuple of the required paramters.
# The client must send a tuple with a list, desired final size of the scrambled list, and the indecies
# that you would like to see elements of. If the input is incorrect, you will recieve an error message.
# Follow the example below:

context =zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

content = "([element1, element2, element3, ...], size_of_result, (index1, index2, ...))"
socket.send_string(content)

# To recieve data from the microservice, use the receive method of the socket created in the request.
# The data must then be decoded which will be represented as a string. The string can be parsed into their respective data types.
# Follow the example below:

message = socket.recv()
string_message = message.decode()

![image](https://github.com/user-attachments/assets/fda13547-a004-4fc2-bf8a-3f665dc3ddfe)
