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
filename = ["a.txt"]

def getFileAddress(_server_ip, _server_port, _message):
	return TalkToServer.getStatus(_server_ip, _server_port, _message)

def bytesToStr(_bytes):
	return str(_bytes, encoding = "utf-8")

def decode(_str):
	return _str.split(":")[:-1]

def getLocation(_list):
	return _list[:2]

def linkNode(_ip, _port, _filename):
	pass 

def listenQuery(_ip, _port):
	link = serverForTest.getLink(_ip, _port)
	print("*" * 10, " nodes is working ", "*" * 10)
	while True:
		serverForTest.listenMessage(link)

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
