# Building a Simple Distributed System

# Assignment Description

This is a distributed chat application that allows users to communicate with each other over a network. The application consists of a server that handles incoming connections from clients and facilitates communication between them.

# Features

1. Allows multiple clients to connect to the server simultaneously
2. Clients can send and receive messages in real-time
3. Server broadcasts messages to all connected clients except the sender
4. Clients can see when other users join or leave the chat

# Instructions

1. Clone the repository to your local machine: git clone https://github.com/schitluri98/DCC-Midterm-Group-3.git
2. Start the server:
   2.1 Open a terminal and run the following command: python server.py
3. Start a client:
   3.1 Open another terminal and run the following command: python client.py
   3.2 Enter your username when prompted
   3.3 Enter the server address (e.g., localhost:8080) when prompted
4. Repeat step 3 to start additional clients and communicate with other users

# Screenshots

1. Start the server in a cluster (localhost:8080, localhost:8081, localhost:8082)
   ![S1](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/52192ba9-fc0a-4dfb-98fb-5a275c00d923)
2. Client Registration
   2.1 Register Client 1 in localhost:8080
   ![S2](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/694717f1-76f7-4ba3-bfd9-97f20f5a45d5)
   2.2 Register Client 2 in localhost:8080
   ![S3](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/d12016fd-c7f4-4ca3-9671-73620c086628)
3. Check if clients are successfully registered with the server.
   ![S5](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/ebe82ad4-c6a3-4809-b3a9-7c2a43a1fbad)
4. Data Sharing
   4.1 Send a message from Client 1
   ![S4](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/5e58e3b1-100c-4ce5-965b-c4c5729c5fa1)
   4.2 Check if the message has been delivered to Client 2
   ![S6](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/fd810728-fbd3-423b-b18e-36293a6f16d4)
   4.3 Send a reply from Client 2
   ![S7](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/057c6d6d-c149-40c3-a6ae-c7b155acf509)
5. Fault Tolerance
   5.1 I explicitly throw an error in the server to see how the system is behaving during data sharing
   ![S8](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/55d524ca-c652-47a2-9d9b-0a5c1e0dd7be)
   5.2 Let's try to send a message from Client 1
   ![S9](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/cca2ec03-e38d-45e9-bca6-41831884f821)
   5.3 It seems like the system is not breaking down and handling the errors properly and data was not shared.
   ![S10](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/17e2285c-3e50-4291-b174-2bd51a0e9102)



   




  
 

