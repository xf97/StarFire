'''
This is a project developed by MeGaCrazy (github: MeGaCrazy), 
who opend the code on github. We noted 
where the source code came from, u
sed it, changed it to suit our needs, 
and implemented our software.
'''

# author = __xiaofeng__
# date = 2019/11/1

'''
节点端修改点：
1. 更改目录结构
上传信息时，添加校验和这一项 done
2. 接收主节点下发的目录结构
3. 当主节点宕机时，使用本地的目录结构的进行通信
'''

#xf added
import sys
import platform #use this library to get current os
sys.path.append("..")
from PeerListener import *
import hashlib  #产生校验和
import os

#节点号
PEER_ID = "0002"



class Peer_Server:  # Connect Peer with Centeral-Server
    def __init__(self):
        print("WELCOME TO PEER TO PEER SHARING FILE SYSTEM\n")
        print("*" * 10, "This is Peer" + PEER_ID[-1:] + " ", "*" * 10)
        while True:
            # Getting Choice From Peer
            Choice = input("TYPE :(1)REGISTER (2) SEARCH (3) DOWNLOAD (4) LIST_ALL (5)LIST_LOCAL_FILES (6)EXIT\n")

            if Choice == REGISTER:
                #Peer_id = input("Enter PEER ID 4 digit: ")  # Getting PEER_ID
                Peer_id = PEER_ID
                self.file_name = input("Enter File name: ")  # Getting file_name will be shared
                content = self.getContent(self.file_name)
                if content == "File does not exist.":
                    print("Stop this registration.")
                else:
                    md5 = self.getMd5(self.file_name, content)
                    self.Peer_port = int(Peer_id)  # Convert Peer_port to int and store as attribute
                    self.registerInServer(md5)  # connect with server and send command to register the file
                    Start_PeerListener(self.Peer_port,
                                   HOST)  # After Register The File Listen to PEER_ID Port for sharing files
                    
            elif Choice == SEARCH:
                self.SearchInServer()  # Connect with server and send command to search for file name


            elif Choice == DOWNLOAD:
                Peer_id = input("Enter PEER ID 4 digit: ")  # Taking PEER_ID and file_name i want to Download file from
                while Peer_id == PEER_ID:
                    Peer_id = input("You cannot download the local file, please enter another node ID: ")
                file_name = input("Enter File name: ")
                self.Download(int(Peer_id), file_name)


            elif Choice == LIST_ALL:  # SHOW ALL Sharing files that registered in Server
                self.List_all()

            elif Choice == EXIT:
                input("enter once to quit.")
                break

            elif Choice == LIST_LOCAL_FILES:
                self.getLocalFiles()

            else:
                print("Wrong choice. please enter another rigth choice.")
                continue
        return

    #overrided by xiaofeng            
    def registerInServer(self, _md5):  # Connect and Send command to Register
        s = socket()
        s.connect((HOST, PORT))
        data = pickle.dumps(self.Regiserdata(self.Peer_port, self.file_name, _md5))
        s.send(data)
        state = s.recv(1024)
        print(state.decode('utf-8'))  # Receive Confirmation of Registration
        s.close()

    def SearchInServer(self):  # Connect and Send command  to Server for Specific File_name
        s = socket()
        s.connect((HOST, PORT))
        file_name = input("Enter File Name : ")
        data = pickle.dumps(self.SearchData(file_name))
        s.send(data)
        ret_data = pickle.loads(s.recv(1024))
        self.print_list(ret_data[0], ret_data[1])  # Return List of Files contain that name
        s.close()

    def List_all(self):  # Connect and Send command to Server to Show all Exiting Files
        s = socket()
        s.connect((HOST, PORT))
        data = pickle.dumps(str(LIST_ALL))
        s.send(data)
        ret_data = pickle.loads(s.recv(1024))
        self.print_list(ret_data[0], ret_data[1])  # Return all exiting files
        s.close()

    #overrided by xiaofeng.
    def Regiserdata(self, Peer_port, file_name, _md5):  # for formatting the return to pickle
        return [REGISTER, Peer_port, file_name, _md5]

    def print_list(self, Files, keys):  # print all List
        if len(Files) > 0:
            print("Peer_Id  |     File_name    |  Checksum | Date_added :\n")
            for item in Files:
                print("  ", item[keys[0]], "   ", item[keys[1]], "   ", item[keys[2]], "   ", item[keys[3]])
        else:
            print("There is no file has this name Or There is no file At all\n")

    def SearchData(self, file_name):  # Command for Search contains file_name, SEARCH indicator command
        return [SEARCH, file_name]

    def Download(self, Peer_id, file_name):  # Connect and Send request for downloading from specific PEER_PORT
        s = socket()
        s.connect((HOST, Peer_id))
        data = pickle.dumps([DOWNLOAD, str(file_name)])
        s.send(data)

        file_path = os.path.join(os.getcwd(), '..')  # Organizing the path of file that will be Download
        file_path = os.path.join(file_path, "Peer" + PEER_ID[-1:] + 'Files')
        file_path = os.path.join(file_path, "downloads")

        with open(os.path.join(file_path, file_name),  # writing to file
                  'wb') as myfile:
            while True:
                data = s.recv(1024)
                if not data:
                    myfile.close()
                    break
                myfile.write(data)
        s.close()
        print('File Downloaded Successfully')
        print(file_name, "is in /Peer", PEER_ID[-1:] + "Files/downloads")

    #xf added
    #get md5 num of file
    def getMd5(self, _filename, _content):
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

    #xf added
    #get file's content
    def getContent(self, _filename):
        #make absolute path
        #judge win or linux
        #now, we couldn't support mac os
        if "windows" in platform.system() or "Windows" in platform.system():
            file_path = "..\\Peer" + PEER_ID[-1:] +"Files\\Uploads\\"  # Organizing the path of file that will be Download
        elif "Linux" in platform.system():
            file_path = "../Peer" + PEER_ID[-1:] + "Files/Uploads/"
        file_path = file_path + str(_filename)
        try:
            f = open(file_path, "r", encoding = "utf-8")
            content = f.read()
            f.close()
        except:
            content = None
            print(file_path, " doesn't exist.")
        if content:
            return content
        else:
            return "File does not exist."

    def getLocalFiles(self):
        if "windows" in platform.system() or "Windows" in platform.system():
            file_path = "..\\Peer" + PEER_ID[-1:] +"Files\\Uploads\\"  # Organizing the path of file that will be Download
        elif "Linux" in platform.system():
            file_path = "../Peer" + PEER_ID[-1:] + "Files/Uploads/"
        localFiles = os.listdir(file_path)
        print("file name:")
        for i in localFiles:
            print(i)
        print()
        print("It's over. You can't share files that don't already exist on your computer. If you want to share new files, just copy them to uploads folder.")


def Start_Peer():
    peer = Peer_Server()  # Start New Peer


if __name__ == '__main__':
    Start_Peer()
