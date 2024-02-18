from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://mail.google.com/login")

username_field = driver.find_element_by_id("username")
username_field.send_keys("your_username")

password_field = driver.find_element_by_id("password")
password_field.send_keys("your_password")

login_button = driver.find_element_by_id("login_button")
login_button.click()
