import socket

ADDRESS = 'localhost' #string o 127.0.0.1
# ADDRESS = '0.0.0.0' para que todos los dispositivos puedan conectarse
PORT = 1234 #int

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((ADDRESS, PORT))
sock.listen()

connection, client_address = sock.accept()

print(f'Received connection from address: {client_address}')
try:
    while True:
        data = connection.recv(1024)

        print(f'Received data: {data.decode()}')
except KeyboardInterrupt:
    print('Closing connection')
except Exception as e:
    print(f'An error occurred: {e}')
finally:
    connection.close()
    sock.close()

# buscar puertos scannear
# sudo install nmap
# sudo nmap <address>
# ifconfi | gerp "inet 1"
