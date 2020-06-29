"""
A simple Python script to send messages to a sever over Bluetooth
using PyBluez (with Python 3.7).
"""

import bluetooth
import time
import zerorpc

#Pyboard = 48:4A:30:01:80:B2, CEEO EV3 = F0:45:DA:15:FB:8D, My EV3 = A0:E6:F8:60:17:5E
serverMACAddress = 'F0:45:DA:15:FB:8D' #change to your EV3 Bluetooth address
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4243")

while 1:
    text = c.message()
    if text == "quit":
        c.response("quit")
        break
    encodedMsg = text.encode('utf-8')
    s.send(encodedMsg)
    data = s.recv(1024)
    #print(data.decode())
    c.response(data.decode())
s.close()