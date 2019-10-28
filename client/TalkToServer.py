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
	#print("l1")
	for i in _list:
		s += str(i)
		s += ":"
	#print("l2")
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

def getStatus(server_ip, server_port, _message):
	retry_code = 1
	suc_code = False
	while retry_code <= 3 and not suc_code:
		s = getLink(server_ip, server_port)
		if s == None:
			print("retry connection, count: ", retry_code)
			retry_code += 1
			continue
		#print("2.1")
		message = listToStr(_message)
		#print("2.2")
		sendMessage(s, message)
		#print("2.3")
		suc_code = True
	if retry_code > 3:
		print("get max connection time, connection abort.")
		return "master node is done."
	else:
		return "master node is ok."
	

#unit test
if __name__ == "__main__":
	print(getStatus(SERVER_IP, SERVER_PORT, tdata))

