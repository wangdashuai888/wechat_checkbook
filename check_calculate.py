#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 20:19:16 2020

@author: taotao
"""
import check_db


def status_check():
	print('进入计算检测')
	return

def calculate(message,trigger,item_price):#识别并计算
	if(trigger == 1):
		people = message[-1].split("@")
		people = people[1:]
		print('people_list:',people)
		people_counter = len(people)
		print('total_people:',people_counter)
		unit_price = item_price / people_counter
		#check_db.item_write(item_price)#新建项写入
		#if(is_comment == 1):
			#return_message = "识别记账输入，记账金额" + str(item_price) + "备注：" + comment + "记账人数" + str(people_counter) + "人均价格" + str(unit_price)
		return_message = "识别记账输入，记账金额" + str(item_price) + "记账人数" + str(people_counter) + "人均价格" + str(unit_price)
	elif(trigger == 2):
	return return_message