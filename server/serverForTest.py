#-*- coding:utf-8 -*-
'''
The server is used to test client
'''

import socket
import sys


#server information
SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999

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
		print("reveicve ", addr, " message.")
		clientsocket.close()
	except:
		print("listenMessage error.")


#unit test
if __name__ == "__main__":
	link = getLink(SERVER_IP, SERVER_PORT)
	while True:
		listenMessage(link)