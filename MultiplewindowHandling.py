from selenium import webdriver
import time

webdriver=webdriver.Chrome(executable_path="C:\\Driver\\chromedriver.exe")
webdriver.get("https://phptravels.com/")
webdriver.maximize_window()
webdriver.implicitly_wait(10)
win_id=webdriver.current_window_handle
# print(win_id)
time.sleep(5)
webdriver.find_element_by_xpath('//*[@id="main-menu"]/ul/li[8]/a/span').click()
mul_win_id=webdriver.window_handles

#USING FOR LOOP

# for id in mul_win_id:
#     if(cur_win_id!=id):
#         webdriver.switch_to.window(id)
#         webdriver.find_element_by_id("inputEmail").send_keys("NIGHTTIGER")
#         print("test case passed")
#         webdriver.close()

print(mul_win_id)
print(type(mul_win_id))
print(mul_win_id[1])
webdriver.switch_to.window(mul_win_id[1])
webdriver.find_element_by_id("inputEmail").send_keys("TIGER")
# webdriver.quit()