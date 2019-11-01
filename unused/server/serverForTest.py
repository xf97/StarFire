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

#test data
tdata = ['a.txt', '127.0.0.1', 'c3b0928605f3bedf2b03996a6438100b', 1572250873.3573701]

def getLink(_server, _port):
	try:
		serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		serversocket.bind((_server, _port))
		serversocket.listen(5)
		return serversocket
	except:
		print("fail to initial server.")
		return None

def mySplit(_str, _char):
	li = list()
	li = _str.split(_char)
	return li

def listToStr(_list):
	answer = str()
	for i in _list:
		answer += str(i)
		answer += ":"
	return answer

def listenMessage(_link):
	try:
		if not _link:
			print("connection errpr.")
			return
		clientsocket, addr = _link.accept()
		print(addr, " has connected.")
		message = clientsocket.recv(BUFFSIZE)
		message = str(message, encoding = "utf-8")
		oriMessage = mySplit(message, ":")[:-1]
		if oriMessage:
			#clientsocket.send("receive your message".encode("utf-8"))
			if len(oriMessage) == 1:
				print("message for query.")
				#arecord = answerQuery(oriMessage[0])
				amessge = listToStr(tdata)
				clientsocket.send(amessge.encode("utf-8"))
			elif len(oriMessage) == 4 or len(oriMessage) == 5:
				print("message for update")
				clientsocket.send("receive your message".encode("utf-8"))
			else:
				print("error message.")
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