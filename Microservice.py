import time
import zmq
import random
import ast

context = zmq.Context()

socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:

    # Waits until a message is received
    message = socket.recv()
    decoded_message = message.decode()
    print(f"Receiving message: {decoded_message}")

    time.sleep(3)

    # Converts message from string
    converted_message = ast.literal_eval(decoded_message)

    # Validates the data in the received message
    if type(converted_message) is tuple:

        try:
            received_data = converted_message[0]

            try:
                size = converted_message[1]

                if size > len(received_data):
                    size = len(received_data)

            except IndexError:
                size = len(received_data)

            try:
                key_pos = converted_message[2]
                temp_pos = []

                for pos in key_pos:

                    if pos < size:
                        temp_pos.append(pos)

                key_pos = temp_pos

            except IndexError:
                key_pos = None

            return_data = []

            # Randomizes the elements of the received array into the return array
            while len(return_data) != size:

                index = random.randint(0, len(received_data) - 1)

                if received_data.count(received_data[index]) > return_data.count(received_data[index]):
                    return_data.append(received_data[index])

            if key_pos is not None:

                pos_message = "{"
                index = 0

                for pos in key_pos:

                    if index < len(key_pos) - 1:
                        pos_message += f"'Index{pos}': '{return_data[pos]}', "
                        index += 1

                    else:
                        pos_message += f"'Index{pos}': '{return_data[pos]}'"

                pos_message += "}"

                content = f'({return_data}, {pos_message})'

            else:
                content = (return_data,)

            print(f"Sent: {str(content)}")
            socket.send_string(str(content))

        except IndexError:
            socket.send_string("ERROR: Invalid Input")

    else:
        socket.send_string("ERROR: Invalid Input")
