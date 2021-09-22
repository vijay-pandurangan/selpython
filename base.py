from selenium import webdriver
import time
#comment
#comment2
driver = webdriver.Chrome()
driver.get("http://www.google.com")
print("Loading the GOOGLE site")
time.sleep(3)
print("Waiting")
driver.maximize_window()
print("Maximizing the window")
time.sleep(4)
driver.quit()
