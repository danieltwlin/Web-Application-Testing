# -*- coding: utf-8 -*-
#=== App Version Lib ============
# Date   : 2019.10.14
# Author : daniel
#================================
import os
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import unittest, time

class AppVersion:
	''' get_version_play( id )
		*取得版本號功能 '''
	def get_version_play(self,id):
		
		driver = webdriver.Chrome()	
		url = 'https://play.google.com/store/apps/details?id=' + id 
		
		# 抓取 paly 版號
		driver.get(url)
		element = driver.find_element_by_xpath(u"//div[text()='目前版本']/../span[1]/div[1]/span[1]")			
		version = element.text
		#print('ver : ' + version)
		
		driver.close()
		
		return version

	''' get_version_biadu( keyword )
		*取得版本號功能 '''
	def get_version_baidu(self,keyword):

		# Web Driver
		driver = webdriver.Chrome()
		
		if(1):	
			# Url
			driver.get('https://shouji.baidu.com/software')
			sleep(1)
			# keyword
			element = driver.find_element_by_xpath('//input[@id ="search"]')
			element.send_keys(keyword)
			
			# 記下當前視窗
			nowhandle = driver.current_window_handle

			# 搜尋
			element = driver.find_element_by_xpath(u'//input[@value="搜索"]')
			element.click()
			sleep(3)	
			
			allhandles = driver.window_handles
			# 選取新視窗	
			for handle in allhandles:		
			#循環判斷窗口是否為當前窗口
				if handle != nowhandle:
					driver.switch_to_window(handle)
					#print('now new window!')
			
			# 點擊 APP
			element = driver.find_element_by_xpath('//a[@class="app-name"]')
			element.click()
			
			# 記下當前視窗
			nowhandle2 = driver.current_window_handle

			allhandles = driver.window_handles
			# 選取新視窗	
			for handle in allhandles:			
			#循環判斷窗口是否為當前窗口
				if handle != nowhandle and handle != nowhandle2:
					driver.switch_to_window(handle)
					#print('now new window!')
					
		if(1):
			element = driver.find_element_by_xpath('//span[@class="version"]')
			version = element.text
			version = version.replace('版本:',' ')
			version = version.strip()	
			#print('version : ' + version)
			
		driver.close()
		
		return version

if __name__ == '__main__':
		
	"""  Demo code  """
		
	myappver = AppVersion()
	
	# play
	if(1):
		id = 'com.android.chrome'
		version = myappver.get_version_play(id)	
		print('version : ' + version)
	
	# baidu
	if(1):
		keyword = 'chrome'	
		version = myappver.get_version_baidu(keyword)
		print('version : ' + version)

	