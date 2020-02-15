#-*- coding:utf-8 -*- 
#! /usr/bin/python

'''
The following program is used to test the Starfire system
'''

__author__ = "xiaofeng"
__date__ = "2019-12-9"

import sys
sys.path.append("../")	#导入父目录

'''
#导入程序
#导入常量文件包
from Constants.Constant import *
#导入服务器端程序
from Server_Codes.Central_Indexed_Server import *
from Server_Codes.OpeDir import *
from Server_Codes.ServerLog import *
#导入客户端1程序
from Peer1_Codes.Peer import *
from Peer1_Codes.PeerListener import *
from Peer1_Codes.clientLogger import *
from Peer1_Codes.OpeDir import *
#导入客户端2程序
from Peer1_Codes.Peer import *
from Peer1_Codes.PeerListener import *
from Peer1_Codes.clientLogger import *
from Peer1_Codes.OpeDir import *
'''

import os

__author1__ = "肖锋"
__author2__ = "张涛"
__author3__ = "张勐"
__email__ = "1506010130@hhu.edu.cn"


class testDriver:
	def __init__(self):
		print("-" * 15, "这里是StarFire使用指导程序", "-" * 15)
		print("-" * 10, "开发、单元测试、集成测试环境: ubuntu 18.04", "-" * 10)
		#print("-" * 15 . "为便于阅读,文字皆使用中文", "-" * 15)
		self.copyRight()
		self.Centralization_1()
		self.Distribution()
		self.Centralization_2()
		self.end()

	def copyRight(self):
		print("作者: ", __author1__, " ", __author2__, " ", __author3__)
		print("邮箱：", __email__)
		print("所有代码和文件皆遵守MIT协议，转载时请注明出处")

	def Centralization_1(self):
		print("-" * 15, "测试阶段1：集中式P2P文件共享系统", "-" * 15)
		input("请跟随如下指令操作, 回车以继续...")
		print("Step 1: 启动中心节点: 请打开Server_Codes文件夹, 使用终端键入以下命令：")
		print("python3 Central-Indexed-Server.py    tips: 在win10下也可双击start.bat批处理文件直接开启两个子节点和服务器节点")
		print("此时,中心节点已经启动.")
		print("此目录下各文件作用为, Central-Indexed-Server.py---服务器主文件, OpeDir.py---目录操作文件, 使得服务器宕机重启后仍然能够读取上一次的目录数据, ServerLog.py---服务器端日志文件, 负责生成服务器的运行日志.")
		self.inputGap()
		print("Step 2: 启动两个测试子节点: 请分别进入Peer1_Codes和Peer2_Codes文件夹, 使用终端键入以下命令(在win10下使用管理员模式打开命令行, 忽略sudo命令)：")
		print("sudo python3 Peer.py")
		print("此目录下各文件作用为, Peer.py---客户端主文件, PeerListener.py---客户端监听文件, OpeDir.py---目录操作文件, clientLogger.py---客户端日志文件")
		print("此时你能在终端中看见子节点的菜单, 本地准备共享的文件在Peer1Files和Pee2Files中的Uploads文件夹中, 已经下载的文件在Peer1Files和Pee2Files中的downloads文件夹中")
		'''
		print("Peer1 准备共享的文件:\t", "已经下载的文件:\t")
		os.system("ls ../Peer1Files/Uploads")
		os.system("ls ../Peer1Files/downloads")
		print("Peer2 准备共享的文件:\t", "已经下载的文件:\t")
		os.system("ls ../Peer2Files/Uploads")
		os.system("ls ../Peer2Files/downloads")
		'''
		print("Step 3: 集中式模式下功能测试")
		print("Step 3.1: 请在两个子节点客户端选择功能５, 查看本地可以上传的文件.　其他功能要在向服务器注册后才可使用.")
		self.inputGap()
		print("Step 3.2: 请在两个子节点客户端选择功能１, 向服务器注册文件,　只可注册本地已有的文件. 若想注册其他文件, 请先将文件移入该节点的Uploads文件夹中. 同一子节点可以多次注册文件, 但注册同一个文件(文件名与内容都相同)时会被拒绝. 放心我们有异常处理机制.")
		self.inputGap()
		print("Step 3.3: 注册后任何功能都可使用, 注意只能下载在中心服务器中注册过的文件, 但是请勿退出子节点程序, 请尝试在Peer1和Pee2中交换文件(推荐在Peer2中下载a.txt, 在Pee1中下载b.txt). 请在测试完所有功能后敲击回车以进入下一测试阶段.")
		self.inputGap()
		print("-" * 15, "测试阶段1：集中式P2P文件共享系统结束", "-" * 15)
		#os.system("python3 ../Server_Codes/Central-Indexed-Server.py")
		#os.system("gnome-terminal -t 'server' -- 'python3 ../Server_Codes/Central-Indexed-Server.py'")

	def Distribution(self):
		print("-" * 15, "测试阶段2：分布式P2P文件共享系统", "-" * 15)
		print("Step 1: 终止中心节点: 请切换到中心节点程序运行的终端, 使用任意办法(推荐ctrl+c或者关掉窗口)终止程序.")
		self.inputGap()
		print("Step 2: 请在任意子节点中使用除5,7之外的任意一个功能(功能5并不连接服务器, 功能7退出程序). 子节点会在三次连接服务器失败后切换到分布式模式运行...")
		self.inputGap()
		print("Step 3: 当子节点切换到分布式模式,　任何功能都可使用, 包括注册新的文件, 但请勿退出子节点程序. 请尝试在Peer1和Pee2中交换文件(推荐在Peer2中下载c.txt, 在Pee1中下载d.txt). 请在测试完所有功能后敲击回车以进入下一测试阶段.")
		self.inputGap()
		print("-" * 15, "测试阶段2：分布式P2P文件共享系统结束", "-" * 15)

	def Centralization_2(self):
		print("-" * 15, "测试阶段3：重新切换至集中式P2P文件共享系统", "-" * 15)
		print("Step 1: 再次启动中心节点: 请打开Server_Codes文件夹, 使用终端键入以下命令：")
		print("python3 Central-Indexed-Server.py")
		print("tips: 可能会报错, 因为之前的服务器程序还在占用端口, 请等待一段时间再试或者杀掉占用5555端口的程序.")
		print("此时, 中心节点再次启动, 启动后会首先读取上次宕机后本地存储的目录文件, 使得数据不丢失.")
		self.inputGap()
		print("Step 2: 按照正常逻辑, 服务器恢复后服务提供商应该通知用户重新连接服务器. 在StarFile中, 我们略过通知用户一步, 请在两个子节点客户端选择功能6重新连接至服务器, 连接成功后子节点会切换到集中式模式工作.")
		self.inputGap()
		print("Step 3: 此时, 系统已恢复到集中式模式, 请测试任意功能. 请尝试在Peer1和Pee2中交换文件(推荐在Peer2中下载e.txt, 在Pee1中下载f.txt). 请在测试完所有功能后敲击回车以进入下一测试阶段.")
		self.inputGap()
		print("-" * 15, "测试阶段3：重新切换至集中式P2P文件共享系统结束", "-" * 15)

	def end(self):
		print("-" * 70)
		print("功能测试已经结束, 请使用功能7退出子节点程序, 请使用任意办法(推荐ctrl+c或者关掉窗口)终止中心节点程序.")
		choice = input("输入1查看当前不足, 输入２直接退出程序: ")
		while choice != "1" and choice != "2":
			choice = input("请输入正确的选项. 输入1查看当前不足, 输入２直接退出程序: ")
		if choice == "1":
			self.shortcoming()
			print("演示结束, 再见!")
			return
		else:
			print("演示结束. 再见!")
			return

	def shortcoming(self):
		print("StarFire当前的不足主要有: ")
		print("1. 当前子节点不注册文件就不能下载东西. StarFire基于一个已有的开源项目开发, 这个问题存在于那个项目中, 我尝试过修复它, 可是一直没做好.")
		print("2. 切换到分布式后无法解决新节点入网问题, 我实在没有多余的时间做这个功能了.")
		print("3. 服务器端和客户端的日志都不能自动清理, 会越来越大, 我的想法是１５天清理一次, 可我也没有时间做这个功能了.")
		print("废话结束, 谢谢使用StarFire!")


	def inputGap(self):
		input("回车以继续...")	

#单元测试模块
if __name__ == "__main__":
	td = testDriver()