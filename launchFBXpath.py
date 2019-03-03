from selenium import webdriver

qspiders = webdriver.Chrome(executable_path="C:\\Driver\\chromedriver.exe")
qspiders.get("https://www.facebook.com/")
qspiders.maximize_window()
qspiders.implicitly_wait(10)
qspiders.find_element_by_xpath("//input[@id='email']").send_keys("admin")
qspiders.find_element_by_xpath("//input[@name='pass']").send_keys("manager")
qspiders.find_element_by_xpath("//input[@type='submit']").click()
qspiders.find_element_by_xpath("//input[@name='firstname']").send_keys("admin")
qspiders.find_element_by_xpath("//input[@name='lastname']").send_keys("manager")