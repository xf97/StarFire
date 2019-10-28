#-*- coding:utf-8 -*-
'''
This module is used to communicate with the master node 
and report local file updates. At the same time, if the 
master node is down, this module also reports down.
'''

#test data
tdata = ['test.txt', '192.168.43.245', 'c3b0928605f3bedf2b03996a6438100b', 1572250873.3573701]

#server information
SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999

import socket

def getLink(_server, _port):
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((_server, _port))
		return s
	except:
		print("Connect master fail.")
		return None

def listToStr(_list):
	s = str()
	for i in _list:
		s += str(i)
		s += ":"
	return s

def sendMessage(_link, _message):
	try:
		bytenum = _link.send(_message.encode("utf-8"))
		if bytenum == 0 :
			print("Fail send.")
		_link.close()
		print("master has reveiced the message ", _message)
	except:
		print("Send message to master fail.")

def getStatus(server_ip, server_port, message):
	

#unit test
if __name__ == "__main__":
	s = getLink(SERVER_IP, SERVER_PORT)
	message = listToStr(tdata)
	sendMessage(s, message)

