from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.google.com")
print("Loading the GOOGLE site")
#time.sleep(6)
time.sleep(3)
print("Waiting")
driver.maximize_window()
print("Maximizing the window")
time.sleep(4)
driver.quit()
