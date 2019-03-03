from selenium import webdriver

qspiders = webdriver.Chrome(executable_path="C:\\Driver\\chromedriver.exe")
qspiders.get("file:///D:/SElenuim%20Demo%20QSPIDER/login.html")
qspiders.maximize_window()
qspiders.implicitly_wait(30)
qspiders.find_element_by_id("123").send_keys("admin")
qspiders.find_element_by_id("456").send_keys("manager")
qspiders.find_element_by_id("111").click()