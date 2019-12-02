#! /usr/bin/python

#__author__ = xiaofeng
#first write date = 2019/12/2

'''
This program is used to add , update , remove directory structures and distribute them.
'''

import pickle
import socket
import sys
import platform
from threading import *

sys.path.append("../")

from Constants.Constant import *


class OpeDir(threading.Thread):
	def __init__(self):
		#Initialize the thread
        threading.Thread.__init__(self)
		self.timeGap = TIME_GAP
		#semaphore
        self.semaphore = Semaphore(MUTEX) 