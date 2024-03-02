import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message != "heartbeat":
                print(message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def send_messages(client_socket, username):
    while True:
        try:
            message = input("Type your Message")
            client_socket.sendall(f"{username}: {message}".encode())
        except Exception as e:
            print(f"Error sending message: {e}")
            break

def main():
    username = input("Enter your username: ")
    server_address = input("Enter server address (e.g., localhost:8080): ")

    try:
        host, port = server_address.split(':')
        port = int(port)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        client_socket.sendall(username.encode())
    except Exception as e:
        print(f"Error connecting to server: {e}")
        return

    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    threading.Thread(target=send_messages, args=(client_socket, username)).start()

if __name__ == "__main__":
    main()
