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

sys.path.append("../")

from Constants.Constant import *


class OpeDir():
	def __init__(self):
		self.timeGap = TIME_GAP
		#semaphore
        self.semaphore = Semaphore(MUTEX)

