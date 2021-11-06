import socket
import time
import json


server = ("localhost", 8200)
client4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
time.sleep(1)
client4.connect(server)
while True:
    
    received_message = client4.recv(1024)
    data = json.loads(received_message.decode())
    data = data.get('a')
    print(data)
    maxNum = max(data)
    client4.send(str(maxNum).encode())
    finalResult = client4.recv(1024)
    print(finalResult)