import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_test import test_login
import time

# def add_plan_test():
#     login = test_login()
#     driver = webdriver.Chrome()
#     wait = WebDriverWait(driver, 10) 
#     driver.get("http://localhost:9000/app/plans")
#     time.sleep(5)
#     driver.get("http://localhost:9000/app/plans/add")
#     name_field = wait.until(EC.presence_of_element_located((By.ID, "id_name")))
#     program_name_field = driver.find_element(By.ID, "id_program_name")
#     name_field.send_keys("New Plan")
#     program_name_field.send_keys("Description of the new plan")
    
# add_plan_test()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_test import test_login 
import time

def add_plan_test():
    driver = test_login()
    if not driver:
        print("Login failed, cannot proceed with adding plan.")
        return

    wait = WebDriverWait(driver, 10)
    driver.find_element(By.CSS_SELECTOR, "#plans .menu-item").click()
    time.sleep(5) 
    driver.find_element(By.ID, "btn-0").click()

    name_field = wait.until(EC.presence_of_element_located((By.ID, "id_name")))
    program_name_field = driver.find_element(By.ID, "id_program_name")

    name_field.send_keys("New Plan")
    program_name_field.send_keys("Description of the new plan")


    submit_button = driver.find_element(By.ID, "submit-button-id")
    submit_button.click()

    success_message = wait.until(EC.presence_of_element_located((By.ID, "success-message-id")))
    print("Plan added successfully")
    driver.quit()

add_plan_test()




# class AddPlanTest(LoginPageTest, unittest.TestCase):
#     def setUp(self):
#         super().setUp()
#         self.test_login()  

#     def test_add_plan(self):
#         driver = self.driver
#         wait = self.wait
#         driver.get("http://localhost:9000/app/plans/add")

#         try:
#             name_field = wait.until(EC.presence_of_element_located((By.ID, "id_name")))
#             program_name_field = driver.find_element(By.ID, "id_program_name")
#             name_field.send_keys("New Plan")
#             program_name_field.send_keys("Description of the new plan")
#             # element = self.driver.find_element(By.CSS_SELECTOR, ".select__control--is-focused > .select__value-container")
#             # actions = ActionChains(self.driver)
#             # actions.move_to_element(element).click_and_hold().perform()

#             dealer_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".select__control--is-focused > .select__value-container")))
#             dealer_dropdown.click()
#             dealer_dropdown.send_keys("arbab talib")
    
#             # wait = WebDriverWait(driver, 10)
#             # dealer_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-7pg0cj-a11yText")))
#             # dealer_dropdown.click()
#             # dealer_dropdown.send_keys("arbab talib")
#             # dealer_option = wait.until(EC.element_to_be_clickable((By.ID, "react-select-11-option-0")))
#             # dealer_option.click()

#             # Interact with the underwriter dropdown
#             # underwriter_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-1gtu0rj-indicatorContainer")))
#             # underwriter_dropdown.click()
#             # underwriter_option = wait.until(EC.element_to_be_clickable((By.ID, "react-select-12-option-0")))
#             # underwriter_option.click()

#             # Interact with the reinsurance dropdown
#             # reinsurance_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-1gtu0rj-indicatorContainer > .css-8mmkcg")))
#             # reinsurance_dropdown.click()
#             # reinsurance_option = wait.until(EC.element_to_be_clickable((By.ID, "react-select-13-option-0")))
#             # reinsurance_option.click()



#             # Click the submit button
#             submit_button = wait.until(EC.element_to_be_clickable((By.ID, "dealer-admin-btn")))
#             submit_button.click()
            
#             # Verify success
#             try:
#                 # Check for a success message
#                 success_message = wait.until(EC.presence_of_element_located((By.ID, "success-message-id")))
#                 self.assertTrue(success_message.is_displayed(), "Success message is not displayed as expected.")

#                 # Alternatively, verify that the plan appears in the list of plans
#                 plans_list = wait.until(EC.presence_of_element_located((By.ID, "plans-list")))
#                 self.assertIn("New Plan", plans_list.text, "The new plan was not added to the plans list.")
#             except NoSuchElementException:
#                 self.fail("Success message or plans list not found.")
#         except ElementClickInterceptedException:
#             self.fail("Element click was intercepted by another element.")
#         except NoSuchElementException:
#             self.fail("Required element was not found on the page.")
#         except Exception as e:
#             self.fail(f"An unexpected error occurred: {e}")

#     def tearDown(self):
#         # Close the browser
#         self.driver.quit()

# if __name__ == "__main__":
#     unittest.main()