#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 19:52:16 2018
@author: taotao
"""
import itchat
import check_db
import check_calculate
from itchat.content import TEXT

@itchat.msg_register(TEXT)#connection check
def status_check(msg):
	if(msg['Text'] == "记账检测20"):
		print('开始记账检测')
		check_db.status_check()
		check_calculate.status_check()

@itchat.msg_register(TEXT,isGroupChat=True)#checkbook trigger
def text_reply(msg):#-[金额][备注][包括/删除][人员]
	trigger = 0#模式识别
	is_comment = 0#检测是否包含备注
	if(msg['Text'][0] == "-"):
		#trigger detection
		message = msg['Text'][1:].split(' ')
		print(message)
		item_price = int(message[0])#获取总价	
		print('Captured Price:',item_price)
		#1 正序 2 全体无备注 3 全体有备注 6 备注排除 4 正序备注 5 排除
		if(len(message) == 1):#全体模式无备注
			trigger = 2
		else:
			if(message[1][0] == "@"):
				trigger = 1
			#elif(message[1][0:1] == "排除"):
				#trigger = 5
			else:#任何无法识别内容默认为备注
				comment = message[1]
				print('识别到备注',comment)
				if(len(message) == 2):
					trigger = 3
				elif(message[2][0] == "@"):
					trigger = 4
				#elif(message[2][0:1] == "排除"):
					#trigger = 6
				else:
					print('识别失败')
		print('识别模式',trigger)
		return_message = check_calculate.calculate(message,trigger,item_price)
		msg.user.send(return_message)

itchat.auto_login()
itchat.run()
itchat.send('开始工作',toUserName='filehelper')