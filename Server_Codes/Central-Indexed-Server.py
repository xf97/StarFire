#! /usr/bin/python
'''
This is a project developed by MeGaCrazy (github: MeGaCrazy), 
who opend the code on github. We noted 
where the source code came from, u
sed it, changed it to suit our needs, 
and implemented our software.
'''

# author = __xiaofeng__
# date = 2019/12/2


#system: ubuntu 18.04

'''
Server-side modification points:
1. Change the directory structure
Existing directory structure = [node id, file name, add date]
Change to directory structure = [node id, file name, checksum, add date] done
2. Add the function interval of distributing files, every 30 seconds
'''


# data persistence store
import pickle
# multithreading library
import threading
from datetime import datetime
from socket import *
from threading import *
import time #Timing module
from ServerLog import ServerLogger  #导入服务器端日志库
import logging

#xf added
import sys
sys.path.append("../")

from Constants.Constant import *


class Server(threading.Thread):
    def __init__(self, port, host, max_connection):
        self.logger = ServerLogger()    #初始化日志记录
    	#Initialize the thread
        threading.Thread.__init__(self)
        self.host = 'localhost'
        #semaphore
        self.semaphore = Semaphore(max_connection)  # For Handling threads synchronization
        self.port = 5555  # this port it will listen to
        self.sock = socket()
        self.sock.bind((self.host, self.port))  # bind socket to address
        self.sock.listen(max_connection)
        #如果有本地目录结构，读取
        try:
            print("Read the local directory structure...", end = " ")
            self.logger.writingLog(logging.INFO, "Read the local directory structure...")
            with open("dir.data", "rb") as file:
                self.Files = pickle.load(file)
            print("\t done")
            self.logger.writingLog(logging.INFO, "\t done")
        except:
            self.Files = []
            print("There is no directory structure locally.")
            self.logger.writingLog(logging.INFO, "There is no directory structure locally.")
        self.keys = ['peer_id', 'file_name', 'Checksum', 'Date_added']
        print("Server Start listening on", self.host, " : ", self.port)

    def run(self):
        while True:
            conn, addr = self.sock.accept()
            #print("Got Connection From ", addr[0], " : ", addr[1])
            self.logger.writingLog(logging.INFO, "Got Connection From " + str(addr[0]) + " : " + str(addr[1]))
            #Decode the data sent by the client
            try:
                request = pickle.loads(conn.recv(1024))
            except:
                continue

            if request[0] == REGISTER:  # Register File and Send Confirmation Msg
                #print("Peer ", addr[1], " ,Add New File\n")
                self.logger.writingLog(logging.INFO, "Peer " + str(addr[1]) +  " ,Add New File")
                self.semaphore.acquire()
                if self.register(request[1], request[2], request[3], str(datetime.now())):
                    ret = "File Registered Successfully,"
                    file = open("dir.data", "wb")
                    pickle.dump(self.Files, file)
                    file.close()
                    self.logger.writingLog(logging.INFO, "The directory structure has been updated.")
                else:
                	ret = "This file has already been registered in the server. Duplicate registration is not allowed."
                conn.send(bytes(ret, 'utf-8'))
                self.semaphore.release()
                conn.close()


            elif request[0] == SEARCH:  # Search for File_Name and return List of Files That Match the name
                #print("Peer ", addr[1], " ,Searching For a File\n")
                self.logger.writingLog(logging.INFO, "Peer " + str(addr[1]) + " ,Searching For a File\n")
                self.semaphore.acquire()
                #Encrypt data before sending it
                #print(self.Search_data(request[1]))
                ret_data = pickle.dumps(self.Search_data(request[1]))
                conn.send(ret_data)
                self.semaphore.release()
                conn.close()



            elif request[0] == LIST_ALL:  # List All Exiting Files and return as a object with pickle
                #print("Peer ", addr[1], " ,Listing all Exiting Files\n")
                self.logger.writingLog(logging.INFO, "Peer " + str(addr[1]) + " ,Listing all Exiting Files\n")
                self.semaphore.acquire()
                ret_data = pickle.dumps(self.all_data())
                conn.send(ret_data)
                self.semaphore.release()
                conn.close()


            else:
                continue

    def register(self, peer_id, file_name, _md5, Date):  # Store all Files in format
        entry = [str(peer_id), file_name, str(_md5), str(Date)]  # peer_id', 'file_name', 'Checksum', 'Date_added'
        #search file, if file's checksum and filename as same as another one.
        #don't register
        for item in self.Files:
        	if item["file_name"] == file_name and item["Checksum"] == _md5:
        		return False
        self.Files.insert(0, dict(zip(self.keys, entry)))
        return True

    def Search_data(self, file_name):  # Return File Match name we Search For
        ret = []
        for item in self.Files:
            if item['file_name'] == file_name:
                entry = [item['peer_id'], item['file_name'], item['Checksum'], item['Date_added']]
                ret.insert(0, dict(zip(self.keys, entry)))
        return ret, self.keys

    def all_data(self):  # Return all Exiting Files
        return self.Files, self.keys



def Start_Server():
    print("Welcome!!..CENTRAL INDEX SERVER IS UP AND RUNNING.\n")
    server = Server(HOST, PORT, 5)  # Start the Central Server
    server.start() #start thread, as same as server.run() but run in another thread
    distrubuteDir(server.all_data()[0])

def getEachPort(_Files):
    s = set()
    #保证下发时不向一个节点下发多次目录
    for i in _Files:
        s.add(i["peer_id"])
    return s

def distrubuteDir(_Files):
    sl = ServerLogger()
    if len(_Files) != 0:
        #print("Time 30 seconds")
        sl.writingLog(logging.INFO, "Time 30 seconds")
        index = 1
        s = getEachPort(_Files)
        for i in s:
            try:
                i_socket = socket() #获取socket对象
                i_socket.connect((HOST, int(i)))    #创建到各个节点的连接
                #加密数据
                file_data = pickle.dumps(_Files)
                i_socket.send(file_data)
                #print("\rDelivery schedule: ", round(float(index) / len(s), 2), end = " ") #进度条
                sl.writingLog(logging.DEBUG, "Delivery schedule: " + str(round(float(index) / len(s), 2)))
                i_socket.close()
                index += 1
            except:
                #print("\rDelivery schedule: ", round(float(index) / len(s), 2), end = " ") #进度条
                sl.writingLog(logging.DEBUG, "Delivery schedule: " + str(round(float(index) / len(s), 2)))
                index += 1  #如果连接节点发生异常，保持正常运行
    else:
        sl.writingLog(logging.INFO, "The directory is empty and no data is sent.")
        #print("The directory is empty and no data is sent.")
    #print()
    threading.Timer(TIME_GAP, distrubuteDir, (_Files,)).start()


if __name__ == '__main__':
    Start_Server()
