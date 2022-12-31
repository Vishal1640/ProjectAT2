from selenium import webdriver
# Importing by class
from selenium.webdriver.common.by import By
# Importing keys
from selenium.webdriver.common.keys import Keys
import time
# Note:
#Using time.sleep instead of implicit wait so that the step by step executions is visble
class new_emp():

    def test(self):

        # Initializing web browser
        driver = webdriver.Firefox()
        base_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        driver.get(base_url)
        # Maximizing the window
        driver.maximize_window()
        driver.implicitly_wait(10)
        # XPath for username
        xpath_for_username = '//input[@name="username"]'
        username_input = driver.find_element(By.XPATH, xpath_for_username)
        # Sending keys for username
        username_input.send_keys("Admin")
        # XPath for password
        xpath_for_password = '//input[@name="password"]'
        password_input = driver.find_element(By.XPATH, xpath_for_password)
        # Sending keys for password
        password_input.send_keys("admin123")
        # Xpath for login
        xpath_for_login = '//button[@type="submit"]'
        click_on_login = driver.find_element(By.XPATH, xpath_for_login)
        # Clicking on login
        click_on_login.click()
        # Switch to admin tab
        xpath_for_admin = '//a[@href="/web/index.php/admin/viewAdminModule"]'
        switch_to_admin = driver.find_element(By.XPATH, xpath_for_admin)
        # Clicking on admin tab
        switch_to_admin.click()
        time.sleep(2)
        # Xpath for switching to PIM tab
        xpath_for_pim = '//a[@href="/web/index.php/pim/viewPimModule"]'
        switch_to_pim = driver.find_element(By.XPATH, xpath_for_pim)
        switch_to_pim.click()
        time.sleep(2)
        # Validating below menu options are displaying in Side pane
        xpath_for_sidepane = '//nav[@class="oxd-navbar-nav"]'
        side_pane = driver.find_element(By.XPATH, xpath_for_sidepane)
        assert side_pane, side_pane.is_displayed()
        print("Validation is successfull")
        time.sleep(2)
        # Xpath for clicking on Add button
        xpath_for_add = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'
        click_on_add = driver.find_element(By.XPATH, xpath_for_add)
        click_on_add.click()
        time.sleep(4)
        # Sending input for first name
        xpath_for_first_name = '//input[@name="firstName"]'
        first_name = driver.find_element(By.XPATH, xpath_for_first_name)
        # Sending keys for first name
        first_name.send_keys("Ricky")
        time.sleep(3)
        # Sending input for middle name
        xpath_for_middle_name = '//input[@name="middleName"]'
        middle_name = driver.find_element(By.XPATH, xpath_for_middle_name)
        # Sending keys for middle name
        middle_name.send_keys("Thomas")
        time.sleep(3)
        # Sending input for last name
        xpath_for_last_name = '//input[@name="lastName"]'
        last_name = driver.find_element(By.XPATH, xpath_for_last_name)
        # Sending keys for last name
        last_name.send_keys("Hughes")
        time.sleep(3)
        # Enable login details
        xpath_for_enabling_login = '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]'
        enabling_login = driver.find_element(By.XPATH,xpath_for_enabling_login)
        # Clicking on login
        enabling_login.click()
        time.sleep(4)
        # Xpath for Username
        username_pim = "//label[text()='Username']/following::div[1]/input"
        time.sleep(3)
        username_input = driver.find_element(By.XPATH, username_pim)
        # Sendking keys for username
        username_input.send_keys("Vishal B")
        time.sleep(3)
        # Enabling status
        xpath_for_enabling_status = '//label[normalize-space()="Enabled"]'
        enable_status = driver.find_element(By.XPATH, xpath_for_enabling_status)
        # Clicking on enabling status
        enable_status.click()
        time.sleep(3)
        # Xpath for password
        password_pim = "//div/label[text()='Password']/following::div[1]/input"
        password_input = driver.find_element(By.XPATH, password_pim)
        time.sleep(3)
        # Sending keys for password
        password_input.send_keys("Ripo@1640")
        # Xpath for Confirming password
        password_confirm_pim = "//div/label[text()='Confirm Password']/following::div[1]/input"
        password_input_confirm = driver.find_element(By.XPATH, password_confirm_pim)
        time.sleep(3)
        # Sending keys for password
        password_input_confirm.send_keys("Ripo@1640")
        time.sleep(3)
        # Xpath for save button
        xpath_for_save = '//button[@type="submit"]'
        save_button = driver.find_element(By.XPATH, xpath_for_save)
        # Clicking on save button
        save_button.click()
        time.sleep(3)
        print("Created new employee and page moved to employee list")
        driver.quit()
abc = new_emp()
abc.test()






        

