import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://acemoneytransfer.com/")

driver.find_element(By.LINK_TEXT, "Login").click()
driver.find_element(By.ID, "email").click()
driver.find_element(By.ID, "email").send_keys("usmankhadim.uk.uk1@gmail.com")
time.sleep(5)

driver.find_element(By.ID, "password").click()
driver.find_element(By.ID, "password").send_keys("muhammadusman1122")
time.sleep(5)

driver.find_element(By.CLASS_NAME, "checkmark").click()
driver.find_element(By.ID, "login").click()

time.sleep(10)
