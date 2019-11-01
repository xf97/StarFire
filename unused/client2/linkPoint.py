#-*- coding:utf-8 -*-
'''
This file serves two purposes:
When the master node is normal, 
it sends information to the master node to get 
the file address, and then receives the response 
from the master node, and establishes a link to 
another child node through the response content.

When the primary node fails, a link to another 
child node is established by detecting the local directory
'''
import sys
import socket
sys.path.append("../server")

import TalkToServer
import serverForTest

#author = __xiaofeng__
#date = 2019/10/30(v0.1)

#server information
SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999
BUFFSIZE = 1024

#another information
ANOTHER_PORT = 10001

#test data
catalog = [["a.txt", "127.0.0.1", 'c3b0928605f3bedf2b03996a6438100b', 1572250873.3573701]]


def bytesToStr(_bytes):
	return str(_bytes, encoding = "utf-8")

def decode(_str):
	return _str.split(":")[:-1]

def getLocation(_list):
	return _list[:2]

def linkNode(_ip, _port, _filename):
	pass 

def getLocalFile(_filename):
	for i in catalog:
		if _filename == i[0]:
			return i
	return list()

def listenMessage(_link):
	if not _link:
		print("connection errpr.")
		return
	clientsocket, addr = _link.accept()
	print(addr, " has connected.")
	message = clientsocket.recv(BUFFSIZE)
	message = str(message, encoding = "utf-8")
	fileInfo = getLocalFile(message)
	clientsocket.send(str(fileInfo).encode("utf-8"))
	clientsocket.close()
	'''
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
	'''

def listenQuery(_ip, _port):
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	serversocket.bind((_ip, _port))
	serversocket.listen(5)
	print("*" * 10, " nodes is working ", "*" * 10)
	while True:
		listenMessage(serversocket)
#unit test
if __name__ == "__main__":
	'''
	answer = getFileAddress(SERVER_IP, SERVER_PORT, filename)
	answer = bytesToStr(answer)
	li = decode(answer)
	li = getLocation(li)
	print(li)
	'''
	listenQuery("127.0.0.1", 10000)
