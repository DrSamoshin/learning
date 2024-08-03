import socket


def server_request(server_ip: str):
    port = 80

    '''
        creating TCP-socket
        AF_INET - use IPv4 address
        SOCK_STREAM - specify, it's TCP-socket.
    '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        '''
            Установление TCP-соединения:
                Клиент устанавливает соединение с сервером по протоколу TCP/IP. Это включает в себя выполнение 
                трехэтапного рукопожатия (TCP three-way handshake):
                •	Клиент отправляет SYN (Synchronize) пакет на сервер.
                •	Сервер отвечает SYN-ACK (Synchronize-Acknowledge) пакетом.
                •	Клиент отвечает ACK (Acknowledge) пакетом, подтверждая установление соединения. 
        '''
        # Establishing a connection to the server
        sock.connect((server_ip, port))
        print(f"connection to {host} on port {port} established.")

        # formation HTTP-request
        request = "GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n"

        # sending HTTP-request
        sock.sendall(request.encode())
        print("HTTP-request is send.")

        # receiving response from server
        response = sock.recv(4096)  # we get up to 4096 bytes
        print("response from server is got up:")
        print(response.decode())

    finally:
        # closing socket
        sock.close()
        print("connection is closed.")


if __name__ == '__main__':
    host = "3.66.219.170"
    server_request(host)
