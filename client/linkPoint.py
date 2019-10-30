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
import TalkToServer

#author = __xiaofeng__
#data = 2019/10/30(v0.1)

#server information
SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999
BUFFSIZE = 1024

#test data
filename = "a.txt"

def getFileAddress(_server_ip, _server_port, _message):
	return TalkToServer.getStatus(_server_ip, _server_port, _message)

#unit test
if __name__ == "__main__":
	print(getFileAddress(SERVER_IP, SERVER_PORT, filename))