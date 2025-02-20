import socket
import threading

def handle_client(client_socket, addr):
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        print(f"Received from {addr}: {data}")

        response = input("Enter your response: ")
        client_socket.send(response.encode('utf-8'))

    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print("[*] Server listening on port 9999")

    while True:
        client, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

        client_handler = threading.Thread(target=handle_client, args=(client, addr))
        client_handler.start()

if __name__ == "__main__":
    start_server()
