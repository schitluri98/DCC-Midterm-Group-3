# Building a Simple Distributed System

## Assignment Description

This is a distributed chat application that allows users to communicate with each other over a network. The application consists of a server that handles incoming connections from clients and facilitates communication between them.

## Features

1. Allows multiple clients to connect to the server simultaneously
2. Clients can send and receive messages in real-time
3. Server broadcasts messages to all connected clients except the sender
4. Clients can see when other users join or leave the chat

## Instructions

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/schitluri98/DCC-Midterm-Group-3.git
   ```
2. Start the server:
   - Open a terminal and run the following command:
     ```
     python server.py
     ```
3. Start a client:
   - Open another terminal and run the following command:
     ```
     python client.py
     ```
   - Enter your username when prompted
   - Enter the server address (e.g., localhost:8080) when prompted
4. Repeat step 3 to start additional clients and communicate with other users

## Screenshots

1. **Start the server in a cluster (localhost:8080, localhost:8081, localhost:8082)**

   ![Screenshot 1](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/52192ba9-fc0a-4dfb-98fb-5a275c00d923)

2. **Client Registration**
   - Register Client 1 in localhost:8080

      ![Screenshot 2](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/694717f1-76f7-4ba3-bfd9-97f20f5a45d5)
   - Register Client 2 in localhost:8080

      ![Screenshot 3](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/d12016fd-c7f4-4ca3-9671-73620c086628)

3. **Check if clients are successfully registered with the server**

    ![Screenshot 5](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/ebe82ad4-c6a3-4809-b3a9-7c2a43a1fbad)

4. **Data Sharing**
   - Send a message from Client 1

      ![Screenshot 4](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/5e58e3b1-100c-4ce5-965b-c4c5729c5fa1)
   - Check if the message has been delivered to Client 2

      ![Screenshot 6](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/fd810728-fbd3-423b-b18e-36293a6f16d4)
   - Send a reply from Client 2
   
     ![Screenshot 7](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/057c6d6d-c149-40c3-a6ae-c7b155acf509)

5. **Fault Tolerance**
   - I explicitly throw an error in the server to see how the system is behaving during data sharing
   
     ![Screenshot 8](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/55d524ca-c652-47a2-9d9b-0a5c1e0dd7be)
   - Let's try to send a message from Client 1
   
     ![Screenshot 9](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/cca2ec03-e38d-45e9-bca6-41831884f821)
   - It seems like the system is not breaking down and handling the errors properly and data was not shared.

     ![Screenshot 10](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/17e2285c-3e50-4291-b174-2bd51a0e9102)

6. **Testing**

   6.1 Interport Communication
   
   - Start the server, which will listen on ports 8080, 8081, and 8082.
     
    ![S11](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/9c9e44e0-a53c-4293-8749-e05520c2213c)

     Client 1 connects to the server using port 8080.
     
     ![S12](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/eb27ea89-c3ea-4473-859f-1a3254926d29)

     Client 2 connects to the server using port 8081.
     
     ![S13](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/3199491a-bbe9-4b37-8dd7-e24d1259aa97)

     Client 1 sends a message to the server, which will broadcast it to all clients, including Client 2.
     
     ![S14](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/60af86d2-b9e1-4ff7-9cb0-06302d039872)

     Client 2 receives the message from the server.
     
     ![S15](https://github.com/schitluri98/DCC-Midterm-Group-3/assets/61785648/b59db4fc-ad0a-4234-9e99-afae2fe8e3c9)


