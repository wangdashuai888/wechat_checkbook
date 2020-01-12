#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 19:52:16 2018
@author: taotao
"""
import itchat
import check_db
from itchat.content import TEXT


@itchat.msg_register(TEXT)#connection check
def status_check(msg):
	if(msg['Text'] == "记账检测"):
		print('开始记账检测')
		check_db.status_check()

@itchat.msg_register(TEXT,isGroupChat=True)#checkbook trigger
def text_reply(msg):#-[金额][备注][包括/删除][人员]
	trigger = 0
	if(msg['Text'][0] == "-"):#trigger detection
		message = msg['Text'][1:].split(' ')
		print(message)
		item_price = int(message[0])#获取总价	
		print('Captured Price:',item_price)
		#识别备注

		#识别操作
		trigger = 1#正序模式

	if(trigger == 1):#trigger 1 output
		people = message[-1].split("@")
		people = people[1:]
		print('people_list:',people)
		people_counter = len(people)
		print('total_people:',people_counter)
		unit_price = item_price / people_counter
		#check_db.item_write(item_price)#新建项写入
		return_message = "识别记账输入，记账金额" + str(item_price) + "记账人数" + str(people_counter) + "人均价格" + str(unit_price)
		msg.user.send(return_message)

itchat.auto_login()
itchat.run()
itchat.send('开始工作',toUserName='filehelper')

