#! /usr/bin/python

'''
Server-side logger
'''

__author__ = "xiaofeng"
__date__ = "2019-12-7"

import logging
import sys

sys.path.append("../")

from Constants.Constant import *

class ServerLogger:
	def __init__(self):
		self.LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "
		self.DATE_FORMAT = '%Y-%m-%d  %H:%M:%S %a '
		logging.basicConfig(level = logging.DEBUG, format = self.LOG_FORMAT,\
			 datefmt = self.DATE_FORMAT, filename = SERVER_LOGNAME)

	def writingLog(self, _type, _msg):
		if _type == logging.DEBUG:
			logging.debug(str(_msg))
		elif _type == logging.INFO:
			logging.info(_msg)
		else:
			logging.error(_msg)



#单元测试模块
if __name__ == "__main__":
	sl = ServerLogger()
	sl.writingLog()
