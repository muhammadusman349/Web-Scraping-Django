import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException

def test_login():
    driver = webdriver.Chrome()
    driver.get("http://localhost:9000/app/login")
    wait = WebDriverWait(driver, 10)

    username = wait.until(EC.presence_of_element_located((By.ID, "login-email")))
    password = driver.find_element(By.ID, "login-password")

    # Enter the credentials
    username.send_keys("dealeradmin@gmail.com")
    password.send_keys("Manage.py2020")

    login_button = wait.until(EC.element_to_be_clickable((By.ID, "dealer-admin-btn")))

    driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
    driver.execute_script("arguments[0].click();", login_button)

    wait = WebDriverWait(driver, 20)

    try:
        wait.until(EC.url_to_be("http://localhost:9000/app/home"))
        print("Login successful, home page loaded.")
    except TimeoutException:
        print("Login failed or home page did not load in time.")
        driver.quit()
        return None

    print(driver.current_url)
    return driver

# Comment out the test login call here, so it doesn't execute during import
# test_login()

# def test_login():
#     driver = webdriver.Chrome()

#     driver.get("http://localhost:9000/app/login")
#     wait = WebDriverWait(driver, 10)
#     username = wait.until(EC.presence_of_element_located((By.ID, "login-email")))
#     password = driver.find_element(By.ID, "login-password")

#     # Enter the credentials
#     username.send_keys("dealeradmin@gmail.com")
#     password.send_keys("Manage.py2020")

#     login_button = wait.until(EC.element_to_be_clickable((By.ID, "dealer-admin-btn")))

#     driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
#     driver.execute_script("arguments[0].click();", login_button)
#     wait = WebDriverWait(driver, 20)

#     try:
#         wait.until(EC.url_to_be("http://localhost:9000/app/home"))
#         print("Login successful, home page loaded.")
#     except TimeoutException:
#         print("Login failed or home page did not load in time.")
#     time.sleep(10)
#     print(driver.current_url)
#     driver.quit()

# test_login()

# driver = webdriver.Chrome()
# driver.get("http://localhost:9000/app/login")
# wait = WebDriverWait(driver, 10)
# username = wait.until(EC.presence_of_element_located((By.ID, "login-email")))
# password = driver.find_element(By.ID, "login-password")
# username.send_keys("dealeradmin@gmail.com")
# password.send_keys("Manage.py2020")
# login_button = wait.until(EC.element_to_be_clickable((By.ID, "dealer-admin-btn")))
# driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
# driver.execute_script("arguments[0].click();", login_button)
# wait.until(EC.url_to_be("/app/home"))
# time.sleep(10)
# driver.quit()


# class LoginPageTest(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("http://localhost:9000/app/login")
#         self.wait = WebDriverWait(self.driver, 3)

#     def test_login(self):
#         driver = self.driver
#         wait = self.wait
#         try:
#             username = wait.until(EC.presence_of_element_located((By.ID, "login-email")))
#             password = driver.find_element(By.ID, "login-password")

#             # Enter the credentials
#             username.send_keys("dealeradmin@gmail.com")  
#             password.send_keys("Manage.py2020")

#             login_button = driver.find_element(By.ID, "dealer-admin-btn")

#             # driver.execute_script("arguments[0].scrollIntoView(true);", login_button)

#             # time.sleep(2)  

#             driver.execute_script("arguments[0].click();", login_button)

#             # time.sleep(5)

#             try:
#                 error_message = wait.until(EC.presence_of_element_located((By.ID, "error-message-id"))) 

#                 self.assertTrue(error_message.is_displayed())
#             except:
#                 self.assertIn("http://localhost:9000/app/home", driver.current_url)
#                 time.sleep(5)

#         except Exception as e:
#             print(f"Test failed: {e}")
#             self.fail("Login test failed")

#     def tearDown(self):
#         self.driver.quit()


# if __name__ == "__main__":
#     unittest.main()
