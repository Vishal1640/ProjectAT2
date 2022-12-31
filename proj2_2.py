from selenium import webdriver
# Importing by class
from selenium.webdriver.common.by import By
# Importing keys
from selenium.webdriver.common.keys import Keys
import time

# Note:
#Using time.sleep instead of implicit wait so that the step by step executions is visble
class orangehrm():

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
        # Validating below menu options are displaying in Side pane
        xpath_for_sidepane = '//nav[@class="oxd-navbar-nav"]'
        side_pane = driver.find_element(By.XPATH, xpath_for_sidepane)
        assert side_pane, side_pane.is_displayed()
        print("Validation is successfull")
        time.sleep(2)
        # Finding xpath for user management tab
        xpath_for_user_mgmt = '//li[@class="oxd-topbar-body-nav-tab --parent --visited"]'
        user_management_tab = driver.find_element(By.XPATH, xpath_for_user_mgmt)
        # Clicking on user management tab
        user_management_tab.click()
        time.sleep(2)
        # Finding xpath for clicking on users
        xpath_for_user = '//a[@href="#"]'
        click_on_user = driver.find_element(By.XPATH, xpath_for_user)
        # Clicking on user management tab
        click_on_user.click()
        # Finding xpath for clicking on user role tab
        click_on_user_role = '//label[text()="User Role"]/following::div[1]'
        users_dropdown = driver.find_element(By.XPATH, click_on_user_role)
        users_dropdown.click()
        # Finding xpath for clicking on admin
        xpath_for_admin = '//div[@role="option"]/span[text()="Admin"]'
        clicking_on_admin = driver.find_element(By.XPATH, xpath_for_admin)
        # Validating to see below drop down value for Users Role dropdown
        if clicking_on_admin.text == "Admin":
            assert clicking_on_admin, clicking_on_admin.text.is_displayed()
            print("Admin is displaying")
        else:
            print("Admin is not displaying")
        # Finding xpath for clicking on ESS
        xpath_for_ESS = '//div[@role="option"]/span[text()="ESS"]'
        clicking_on_ess = driver.find_element(By.XPATH, xpath_for_ESS)
        # Validating to see below drop down value for Users Role dropdown
        if clicking_on_ess.text == "ESS":
            assert clicking_on_ess, clicking_on_ess.text.is_displayed()
            print("ESS is displaying")
        else:
            print("ESS is not displaying")
        time.sleep(2)
        # Finding xpath for clicking on status tab
        click_on_status = '//label[text()="Status"]/following::div[1]'
        status_dropdown = driver.find_element(By.XPATH, click_on_status)
        status_dropdown.click()
        # Finding xpath for selecting enabled
        xpath_for_enabled = '//div[@role="option"]/span[text()="Enabled"]'
        selecting_enabled = driver.find_element(By.XPATH, xpath_for_enabled)
        # Validating to see below drop down value for Status dropdown
        if selecting_enabled.text == "Enabled":
            assert selecting_enabled, selecting_enabled.text.is_displayed()
            print("Enable is displaying")
        else:
            print("Enable is not displaying")
        # Finding xpath for selecting disabled
        xpath_for_disabled = '//div[@role="option"]/span[text()="Disabled"]'
        selecting_disabled = driver.find_element(By.XPATH, xpath_for_disabled)
        # Validating to see below drop down value for Status dropdown
        if selecting_disabled.text == "Disabled":
            assert selecting_disabled, selecting_disabled.text.is_displayed()
            print("Disable is displaying")
        else:
            print("Disable is not displaying")
        driver.quit()   
abc = orangehrm()
abc.test()







