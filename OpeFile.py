#-*- coding:utf-8 -*-
'''
This file is used for file operations.
Warning:
This program in the win10 system debugging, 
not in other operating system environment test availability.
'''

File_Address_data_tructure = ["FileName", "IPAddress", "CheckSum", "Timestamp"]


#author = __xiaofeng__
#version = v0.1(2019/10/27)

import time
import socket 
import hashlib
import os

#get localhost ip address
def getIp():
	myname = socket.getfqdn(socket.gethostname())
	myaddr = socket.gethostbyname(myname)
	return myaddr

#get file md5 (checksum)
#why i choose md5?
#secrity: sha256 > sha1 > md5
#speed: md5 < sha1 <sha256
#Because the md5 algorithm is difficult to break, but faster
def getMd5(_filename, _content):
	try:
		m = hashlib.md5()
		icontent = str(_filename + _content)
		ucontent = icontent.encode(encoding = "utf8")
		m.update(ucontent)
		str_md5 = m.hexdigest()
		return str_md5
	except:
		print(_filename, " md5 failed.")
		return "md5 failed"

#return a record
def getNewRecord(_filename, _content):
	#print("2.1")
	ltime = time.time()
	#print("2.2")
	ip = getIp()
	#print("2.3")
	md5 = getMd5(_filename, _content)
	#print("2.4")
	record = list()
	record.append(_filename)
	record.append(ip)
	record.append(md5)
	record.append(ltime)
	return record



def createFile(_filename, _initContent = ""):
	try:
		if os.path.exists(_filename):
			print("file exists, deleting original file.")
		print("1")
		f = open(_filename, "w", encoding = "utf8")
		f.write(_initContent)
		print("2")
		f.close()
		nRecord = getNewRecord(_filename, _initContent)
		print("3")
		print(nRecord)
	except:
		print("Create file fail.")

def appendFile(_filename, _content):
	try:
		if not os.path.exists(_filename):
			print("file doesn't exist, appending fail.")
			return 
		f = open(_filename, "a", encoding = "utf8")
		f.write(_content)
		f.close()
		f = open(_filename, "r", encoding = "utf8")
		uRecord = getNewRecord(_filename, f.read())
		f.close()
		print(uRecord)
	except:
		print("Update file fail.")

def deleteFile(_filename):
	try:
		if not os.path.exists(_filename):
			print("file doesn't exist, deleting fail.")
			return
		choice = input("Are you sure to delete this file? (y/n)")
		while choice != "y" and choice != "n":
			choice = input("Are you sure to delete this file? (y/n)")
		if choice == "y":
			f = open(_filename, "r" , encoding="utf8")
			dRecord = getNewRecord(_filename, f.read())
			f.close()
			dRecord.append("delete file")
			print(dRecord)
			os.remove(_filename)
		else:
			print("Abort delete.")
	except:
		print("Delete file faile.")



#uint test
if __name__ == "__main__":
	#createFile("test.txt", "hello world")
	#appendFile("test2.txt", "hello world1")
	#deleteFile("test.txt")