import socket
import time
import json
import numpy as np


data= np.arange(1, 17).reshape(4,4)
data = data.tolist()

print("Waiting for the clients")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind(("localhost", 8200))
server.listen(4)

client1 = None
client2 = None
client3 = None
client4 = None


finalList = [0,0,0,0]

while (client1 == None or client2 == None or client3 == None or client4 == None):
    client, address = server.accept()
    # print(clients)
    if(client1 == None):
        client1 = client
        print("Client 1 is online")
        client1.send(json.dumps({"a": data[0], }).encode())
        maxNum = client1.recv(1024)
        finalList[0] = int(maxNum)
        print(maxNum)
    elif(client2 == None):
        client2 = client
        print("Client 2 is online")
        client2.send(json.dumps({"a": data[1], }).encode())
        maxNum= client2.recv(1024)
        finalList[1] = int(maxNum)
        print(maxNum)

    elif(client3 == None):
        client3 = client
        print("Client 3 is online")
        client3.send(json.dumps({"a": data[2], }).encode())
        maxNum= client3.recv(1024)
        finalList[2] = int(maxNum)
        print(maxNum)
    else:
        client4 = client
        print("Client 4 is online")
        client4.send(json.dumps({"a": data[3], }).encode())
        maxNum = client4.recv(1024)
        finalList[3] = int(maxNum)
        print(maxNum)
clients = {"client1_" : client1, "client2_" : client2, "client3_" : client3, "client4_" : client4}
minNum = min(finalList)
# print(clients)
for client_ in clients:
    client = clients[client_]
    client.send(str(minNum).encode())
time.sleep(100)
    
