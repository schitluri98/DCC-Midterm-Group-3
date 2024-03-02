# Building a Simple Distributed System

# Assignment Description

This is a distributed chat application that allows users to communicate with each other over a network. The application consists of a server that handles incoming connections from clients and facilitates communication between them.

# Features

1. Allows multiple clients to connect to the server simultaneously
2. Clients can send and receive messages in real-time
3. Server broadcasts messages to all connected clients except the sender
4. Clients can see when other users join or leave the chat

# Instructions

1. Clone the repository to your local machine:
  • git clone https://github.com/your_username/distributed-chat.git
2. Navigate to the project directory: cd distributed-chat
3. Start the server:
  • Open a terminal and run the following command: python server.py
4. Start a client:
  • Open another terminal and run the following command: python client.py
  • Enter your username when prompted
  • Enter the server address (e.g., localhost:8080) when prompted
5. Repeat step 4 to start additional clients and communicate with other users
