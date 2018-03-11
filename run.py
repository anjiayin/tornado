from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\\Python\\Coding\\tornado\\chromedriver.exe")
driver.get('http://www.chechebijia.com/login')
name_field = driver.find_element_by_id('form-control login_name focus login_form')  # 用户名输入框
password_field = driver.find_element_by_id('form-control login_password focus login_form ')  # 密码输入框
submit_button = driver.find_element_by_id('btn btn-default width btn_login')  # 登录键
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


