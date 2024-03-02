import socket
import threading
import time

class Server:
    def __init__(self, port, servers):
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = {}
        self.running = True
        self.servers = servers

    def start(self):
        print(f"Server on port {self.port} is running.")
        self.server_socket.bind(('localhost', self.port))
        self.server_socket.listen(5)
        threading.Thread(target=self.client_heartbeat).start()  # Start heartbeat thread
        while self.running:
            client_socket, addr = self.server_socket.accept()
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def stop(self):
        self.running = False
        self.server_socket.close()

    def handle_client(self, client_socket):
        username = client_socket.recv(1024).decode()
        self.clients[username] = client_socket
        print(f"{username} has joined the chat.")
        try:
            while True:
                message = client_socket.recv(1024).decode()
                if not message:
                    break
                elif message.startswith("share"):
                    self.share_data(message, username)
                    client_socket.sendall("Data shared successfully".encode())  # Acknowledgment message
                else:
                    self.broadcast_message(message, username)
        except Exception as e:
            print(f"Error with client {username}: {e}")
        finally:
            self.remove_client(username)
            client_socket.close()

    def broadcast_message(self, message, sender):
        for server in self.servers:
            for client_username, client_socket in server.clients.items():
                if client_username != sender:
                    try:
                        client_socket.sendall(f"{sender}: {message}".encode())
                    except Exception as e:
                        print(f"Error sending message to {client_username} on port {server.port}: {e}")

    def share_data(self, message, sender):
        _, recipient, data = message.split(" ", 2)
        for server in self.servers:
            if recipient in server.clients:
                try:
                    server.clients[recipient].sendall(f"{sender} shared: {data}".encode())
                except Exception as e:
                    print(f"Error sending data to {recipient} on port {server.port}: {e}")

    def client_heartbeat(self):
        while self.running:
            time.sleep(5)  # Check every 5 seconds
            dead_clients = []
            for username, client_socket in self.clients.items():
                try:
                    client_socket.sendall("heartbeat".encode())
                except Exception as e:
                    print(f"Error sending heartbeat to {username}: {e}")
                    dead_clients.append(username)
            for username in dead_clients:
                self.replicate_client(username)
                self.remove_client(username)
                print(f"{username} has left the chat (server failure).")

    def replicate_client(self, username):
        for server in self.servers:
            if server.port != self.port:
                try:
                    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client_socket.connect(('localhost', server.port))
                    client_socket.sendall(f"{username} has joined the chat.".encode())
                    server.clients[username] = client_socket
                    print(f"Replicated {username} to server {server.port}")
                    break
                except Exception as e:
                    print(f"Error replicating {username} to server {server.port}: {e}")

    def remove_client(self, username):
        for server in self.servers:
            if username in server.clients:
                server.clients[username].close()
                del server.clients[username]
                print(f"{username} has left the chat.")

def main():
    servers = []
    for port in range(8080, 8083):
        servers.append(Server(port, servers))
    
    for server in servers:
        threading.Thread(target=server.start).start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        for server in servers:
            server.stop()

if __name__ == "__main__":
    main()
