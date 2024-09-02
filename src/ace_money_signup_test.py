from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://acemoneytransfer.com/")

driver.find_element(By.LINK_TEXT, "Create An Account").click()
driver.find_element(By.ID, "email-sign").click()
driver.find_element(By.ID, "email-sign").send_keys("usmankhadim11@gmail.com")
driver.find_element(By.ID, "password").click()
driver.find_element(By.ID, "password").send_keys("muhammadusman1122")
driver.find_element(By.CSS_SELECTOR, "#select2-country_iso_code-container > .select2-selection__placeholder").click()
time.sleep(2)

dropdown_option = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//li[contains(@class, 'select2-results__option') and contains(span, 'Australia')]")))
dropdown_option.click()

driver.find_element(By.CSS_SELECTOR, ".iti__selected-flag > .iti__flag").click()
driver.find_element(By.CSS_SELECTOR, "#iti-0__item-pk > .iti__country-name").click()
driver.find_element(By.ID, "phone").click()
driver.find_element(By.ID, "phone").send_keys("03487567270")
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "#select2-send_to-container > .select2-selection__placeholder").click()
dropdown_option = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//li[contains(@class, 'select2-results__option') and contains(span, 'Pakistan')]")))
dropdown_option.click()
time.sleep(5)

driver.find_element(By.CSS_SELECTOR, "#select2-heared_from-container > .select2-selection__placeholder").click()
dropdown_option = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//li[contains(@class, 'select2-results__option') and contains(., 'Family & Friends')]")))
dropdown_option.click()

# driver.find_element(By.CLASS_NAME, "checkmark").click()
driver.find_element(By.CSS_SELECTOR, "#customer_consent_modal_button > .ladda-label").click()
driver.find_element(By.CSS_SELECTOR, ".aggree-all-checkbox").click()
button = driver.find_element(By.ID, "register_btn")
button.click()

time.sleep(10)
