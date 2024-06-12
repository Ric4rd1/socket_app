import socket
import time

# ADDRESS = 'localhost' #string
ADDRESS = '192.168.10.204'
PORT = 3333 #int

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ADDRESS, PORT))

try:
    while True:
        to_send = input('Enter data to send: ')
        sock.send(to_send.encode())
        time.sleep(1)
except KeyboardInterrupt:
    print('Closing connection')
except Exception as e:
    print(f'An error occurred: {e}')
finally:
    sock.close()