from selenium import webdriver
import time

#TEST PR branch

driver = webdriver.Chrome()
driver.get("http://www.google.com")
print("Loading the GOOGLE site")
time.sleep(3)
time.sleep(1)
print("Waiting")
driver.maximize_window()
print("Maximizing the window")
time.sleep(10)
driver.quit()
