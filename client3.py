import socket
import time
import json


server = ("localhost", 8200)
client3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
time.sleep(1)
client3.connect(server)
while True:
    received_message = client3.recv(1024)
    data = json.loads(received_message.decode())
    data = data.get('a')
    print(data)
    maxNum = max(data)
    client3.send(str(maxNum).encode())
    finalResult = client3.recv(1024)
    print(finalResult)