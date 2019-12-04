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

#xf added
import sys
sys.path.append("../")

from Constants.Constant import *


class Server(threading.Thread):
    def __init__(self, port, host, max_connection):
    	#Initialize the thread
        threading.Thread.__init__(self)
        self.host = 'localhost'
        #semaphore
        self.semaphore = Semaphore(max_connection)  # For Handling threads synchronization
        self.port = 5555  # this port it will listen to
        self.sock = socket()
        self.sock.bind((self.host, self.port))  # bind socket to address
        self.sock.listen(max_connection)
        self.Files = []
        self.keys = ['peer_id', 'file_name', 'Checksum', 'Date_added']
        print("Server Start listening on", self.host, " : ", self.port)

    def run(self):
        while True:
            conn, addr = self.sock.accept()
            print("Got Connection From ", addr[0], " : ", addr[1])
            #Decode the data sent by the client
            request = pickle.loads(conn.recv(1024))

            if request[0] == REGISTER:  # Register File and Send Confirmation Msg
                print("Peer ", addr[1], " ,Add New File\n")
                self.semaphore.acquire()
                if self.register(request[1], request[2], request[3], str(datetime.now())):
                	ret = "File Registered Successfully,"
                else:
                	ret = "This file has already been registered in the server. Duplicate registration is not allowed."
                conn.send(bytes(ret, 'utf-8'))
                self.semaphore.release()
                conn.close()


            elif request[0] == SEARCH:  # Search for File_Name and return List of Files That Match the name
                print("Peer ", addr[1], " ,Searching For a File\n")
                self.semaphore.acquire()
                #Encrypt data before sending it
                #print(self.Search_data(request[1]))
                ret_data = pickle.dumps(self.Search_data(request[1]))
                conn.send(ret_data)
                self.semaphore.release()
                conn.close()



            elif request[0] == LIST_ALL:  # List All Exiting Files and return as a object with pickle
                print("Peer ", addr[1], " ,Listing all Exiting Files\n")
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

def distrubuteDir(_Files):
    if len(_Files) != 0:
        print("Time 30 seconds")
        index = 1
        for i in _Files:
            #获取每个节点监听的端口
            i_port = i["peer_id"]
            i_socket = socket() #获取socket对象
            i_socket.connect((HOST, int(i_port)))    #创建到各个节点的连接
            #加密数据
            file_data = pickle.dumps(_Files)
            i_socket.send(file_data)
            print("\rDelivery schedule: ", round(float(index) / len(_Files), 2), end = " ") #进度条
            i_socket.close()
            index += 1
    else:
        print("The directory is empty and no data is sent.")
    print()
    threading.Timer(TIME_GAP, distrubuteDir, (_Files,)).start()


if __name__ == '__main__':
    Start_Server()
