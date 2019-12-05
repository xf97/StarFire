#! /usr/bin/python

'''
This part of the program is used to manipulate the local directory structure
'''

__author__ = "xiaofeng"
__date__ = "2019-12-5"

import pickle
import time
from datetime import datetime

class OpeDir:
	def __init__(self):
		self.filename = "dir.data"
		with open(self.filename, "rb") as file:
			self.dir = pickle.load(file)

	def insertRecord(self, _record):
		peer_md5 = self.getAllMd5()
		if _record[3] in peer_md5:
			print("The record already exists.")
		else:
			#构造新记录
			new_record = {"peer_id": str(_record[1]), "file_name": _record[2], "Checksum": \
			_record[3], "Date_added": str(datetime.now())}
			#插入新记录
			self.dir.append(new_record)
			#写入存储
			self.writeDirToFile()
			print("A new record has been registered. ", new_record["peer_id"], " ", new_record["file_name"])

	def writeDirToFile(self):
		with open(self.filename, "wb") as file:
			pickle.dump(self.dir, file)
		return

	def getAllMd5(self):
		s = set()	#声明为集合的目的为无重复值
		for i in self.dir:
			s.add(i["Checksum"])
		return s