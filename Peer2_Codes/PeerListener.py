'''
This is a project developed by MeGaCrazy (github: MeGaCrazy), 
who opend the code on github. We noted 
where the source code came from, u
sed it, changed it to suit our needs, 
and implemented our software.
'''

# author = __xiaofeng__
# date = 2019/11/1


import os
import pickle
import threading
from socket import *
from threading import Semaphore
import platform

#xf added
import sys
sys.path.append("..")

from Constants.Constant import *

PEER_ID = "0002"


class PeerListener(threading.Thread):
    def __init__(self, port, host, max_connection):
        threading.Thread.__init__(self)
        self.host = host
        self.semaphore = Semaphore(max_connection)  # For Handling threads synchronization
        self.port = port  # this port it will listen to
        self.sock = socket()
        #不能重复绑定，添加异常捕获，
        #重复绑定时，捕获异常，偏移端口
        try:
            self.sock.bind((self.host, self.port))  # bind socket to address
            self.sock.listen(max_connection)
        except:
            new_port = hash(str(self.port)) % 10000
            self.sock.bind((self.host, new_port))  # bind socket to address
            self.sock.listen(max_connection)
            print("The port is already in use. we change your port to another one: ", new_port)

    def run(self):
        print("And This Peer is Ready For Sharing his File\n")
        while True:
            conn, addr = self.sock.accept()
            print("Got Connection From ", addr[0], " : ", addr[1])
            request = pickle.loads(conn.recv(1024))
            if request[0] == DOWNLOAD:  # Organizing the path of file that will be shared
                '''
                file_path = os.path.join(os.getcwd(), '..')
                file_path = os.path.join(file_path,  "Peer" + PEER_ID[-1:] + 'Files')
                file_path = os.path.join(file_path, "Uploads")
                '''
                file_name = request[1]
                if "windows" in platform.system() or "Windows" in platform.system():
                    file_path = "..\\Peer" + PEER_ID[-1:] +"Files\\Uploads\\" + file_name  # Organizing the path of file that will be Download
                elif "Linux" in platform.system():
                    file_path = "../Peer" + PEER_ID[-1:] + "Files/Uploads/" +file_name
                Full_path = file_path
                self.semaphore.acquire()

                with open(Full_path, "rb") as myfile:       # Start Transfer File to Other Peer
                    while True:
                        l = myfile.read(2014)
                        while (l):
                            conn.send(l)
                            l = myfile.read(1024)
                        if not l:
                            myfile.close()
                            conn.close()
                            break
                self.semaphore.release()
                print('File Sent')
                print("Please make another choice: ")
            else:
                continue


def Start_PeerListener(port, host):
    peer = PeerListener(port, host, 5)  # Start Thread listen to peer_id to share the files with others Peers
    peer.start()
