#-*- coding:utf-8 -*-
'''
The server is used to test client
'''

#author = __xiaofeng__
#version = v0.1(2019/10/28)

import socket
import sys


#server information
SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999
BUFFSIZE = 1024

def getLink(_server, _port):
	try:
		serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		serversocket.bind((_server, _port))
		serversocket.listen(5)
		return serversocket
	except:
		print("fail to initial server.")
		return None

def listenMessage(_link):
	try:
		clientsocket, addr = _link.accept()
		print(addr, " has connected.")
		message = clientsocket.recv(BUFFSIZE)
		if message:
			clientsocket.send("receive your message".encode("utf-8"))
			print(message)
		else:
			print(addr, " doesn't send data.")
		clientsocket.close()
	except:
		print("listenMessage error.")


#unit test
if __name__ == "__main__":
	link = getLink(SERVER_IP, SERVER_PORT)
	print("*" * 10, " server is working ", "*" * 10)
	while True:
		listenMessage(link)