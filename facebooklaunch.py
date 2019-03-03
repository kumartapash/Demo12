from selenium import webdriver

qspiders = webdriver.Chrome(executable_path="C:\\Driver\\chromedriver.exe")
qspiders.get("https://www.facebook.com/")
qspiders.maximize_window()
qspiders.implicitly_wait(30)
qspiders.find_element_by_id("email").send_keys("facebooklogin")
qspiders.find_element_by_id("pass").send_keys("password")
qspiders.find_element_by_id("u_0_2").click()