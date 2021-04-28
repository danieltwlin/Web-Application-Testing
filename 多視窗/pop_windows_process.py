
#獲得當前窗口
nowhandle = driver.current_window_handle
#獲得所有窗口
allhandles = driver.window_handles
#循環判斷窗口是否為當前窗口
	for handle in allhandles:
		print( 'len : ' + str(len(allhandles)))
		
		if( handle != nowhandle):
			driver.switch_to_window(handle)
			print('now new window!')

			sleep(wait_time)
			# 鉤選第一個老師
			inputElements = driver.find_elements_by_name("arr_MemberID[]")
			inputElements[0].click()
			#捲動視窗
			driver.execute_script("window.scrollTo(0,1000)")
			sleep(wait_time)
			# 新增鉤選的科任老師
			inputElement = driver.find_element_by_xpath("//input[@onclick='JavaScript:AddConfirm()';")
			inputElement.click()
			sleep(wait_time)
			# 修改完成，關閉窗口
			inputElement = driver.find_element_by_xpath("//input[@onclick='javascript:Confirm()']")
			sleep(wait_time)

      # 回到原本窗口
			driver.switch_to_window(nowhandle)
      break;	  # 跳出迴圈，不然會有奇怪的狀況



視窗最大化
dr.maximize_window()

捲動視窗
dr.execute_script("window.scrollTo(0,1000);")
