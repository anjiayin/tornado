import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#path = "D:\\Python\\Coding\\tornado\\chromedriver.exe"
path = "E:\\Coding\\tornado\\chromedriver.exe"

driver = webdriver.Chrome(executable_path = path)
driver.get('http://www.chechebijia.com/login')
# 在获取网页后
'''WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, 'loginName'))) '''
# 等待 id 为 loginName的元素出现，最多20秒
time.sleep(1)

name_field = driver.find_element_by_class_name('login_name')  # 用户名输入框
password_field = driver.find_element_by_class_name('login_password')  # 密码输入框
submit_button = driver.find_element_by_class_name('btn-default')  # 登录键
name_field.clear()
name_field.send_keys('13811848104')
password_field.clear()
password_field.send_keys('cnt82562288')
submit_button.click()
driver.get_cookies()
for cookie in driver.get_cookies():
    #another_driver.add_cookie(cookie)
    print(type(cookie))
    print(cookie)




