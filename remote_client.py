import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = input("Enter the server IP address: ")
    server_port = 9999

    client.connect((server_ip, server_port))

    while True:
        message = input("Enter a message: ")
        client.send(message.encode('utf-8'))

        response = client.recv(1024).decode('utf-8')
        print(f"Received from server: {response}")

    client.close()

if __name__ == "__main__":
    start_client()
