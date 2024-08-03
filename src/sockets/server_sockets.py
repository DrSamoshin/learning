import socket


def server_socket_running():
    # port 80 demands admin permissions, maybe you need to use sudo for running this script.
    PORT = 80
    HOST = '0.0.0.0'  # listening on all interfaces

    # create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Параметр socket.SO_REUSEADDR позволяет повторно использовать адрес и порт
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Привязка сокета к адресу и порту
    server_socket.bind((HOST, PORT))

    # Начало прослушивания входящих соединений
    server_socket.listen(5)
    print(f"server is run and listening port {PORT}")

    try:
        while True:
            # accepting an incoming connection
            client_socket, client_address = server_socket.accept()
            print(f"connection is created with {client_address}")

            # getting client data
            request = client_socket.recv(1024).decode()
            print(f"request is got:\n{request}")

            # forming HTTP-response
            http_response = """\
    HTTP/1.1 200 OK
    Content-Type: text/plain
    
    Hello, this is a response from your Python server!
    """
            # sending HTTP-response to client
            client_socket.sendall(http_response.encode())

            # closing connection with client
            client_socket.close()

    finally:
        # closing server socket
        server_socket.close()
        print("server is stopped.")


if __name__ == '__main__':
    server_socket_running()