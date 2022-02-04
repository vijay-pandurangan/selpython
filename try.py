from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://selectorshub.com/xpath-practice-page/")
driver.maximize_window()
time.sleep(2)

#Enabling the viewbox
driver.find_element_by_xpath("//label[normalize-space()='Can you enter name here through automation']//*[name()='svg']").click()

#Entering the first name
driver.find_element_by_xpath("//input[@placeholder='First Enter name']").send_keys("RELEASE")

#Entering the last name using Javascript executor
last_name = driver.find_element_by_xpath("//input[@placeholder='Enter Last name']")
driver.execute_script("arguments[0].value='ADMINISTRATOR';",last_name)

time.sleep(4)

driver.quit()
