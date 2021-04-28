# Switch new windows , (限用只有兩個 Windows 的情況)
def switch_new_windows(driver,before_window_handle ):
	
	nowhandle = before_window_handle
	#記住點擊後窗口
	nowhandle2 = driver.current_window_handle
	
	if( nowhandle == nowhandle2 ):
		print("current windows is still the same")
		
		#獲得所有窗口
		allhandles = driver.window_handles
		#循環判斷窗口是否為當前窗口
		
		print('len : ' + str(len(allhandles)))
		
		# 換成新的視窗
		for handle in allhandles:
			if( handle != nowhandle):
				print('swith to new windows!')
				driver.switch_to_window(handle)
				print('Already switch new window!')
	else:
		print("current windows is new windows")


#記住現在窗口
	nowhandle = driver.current_window_handle
	
	# 點擊影片button
	btns = driver.find_elements_by_xpath("//button")
	print(len(btns))
	btns[0].click()				

# 切換成新分頁
switch_new_windows(driver,nowhandle)

# p.s 請記得先更新成新的 web driver 
