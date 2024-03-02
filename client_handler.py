import threading
import socket

class ClientHandler(threading.Thread):
    def __init__(self, client_socket, username, clients):
        super().__init__()
        self.client_socket = client_socket
        self.username = username
        self.clients = clients

    def run(self):
        try:
            while True:
                message = self.client_socket.recv(1024).decode()
                if not message:
                    break
                self.broadcast_message(message)
        except Exception as e:
            print(f"Error with client {self.username}: {e}")
        finally:
            self.client_socket.close()
            self.remove_client()

    def broadcast_message(self, message):
        for client_username, client_socket in self.clients.items():
            if client_username != self.username:
                try:
                    client_socket.sendall(message.encode())
                except Exception as e:
                    print(f"Error sending message to {client_username}: {e}")

    def remove_client(self):
        del self.clients[self.username]
        print(f"{self.username} has left the chat.")
