import zmq
import ast

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

content = str((["A", "B", "C", "D", "E", "F"], 3, (1, 2)))

print(f"Sending message: {content}")
socket.send_string(content)

message = socket.recv()
print(f"Received: {message.decode()}")

print(f"Parsed data: {ast.literal_eval(message.decode())}")
