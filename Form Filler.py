from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.example.com/signup")

name_field = driver.find_element_by_name("name")
name_field.send_keys("John Doe")

email_field = driver.find_element_by_name("email")
email_field.send_keys("johndoe@example.com")

submit_button = driver.find_element_by_css_selector(".submit-button")
submit_button.click()
