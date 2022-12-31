from selenium import webdriver
# Importing by class
from selenium.webdriver.common.by import By
# Importing keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import time

# Note:
#Using time.sleep instead of implicit wait so that the step by step executions

class job_details():

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
        # Xpath for switching to PIM tab
        xpath_for_pim = '//a[@href="/web/index.php/pim/viewPimModule"]'
        switch_to_pim = driver.find_element(By.XPATH, xpath_for_pim)
        switch_to_pim.click()
        time.sleep(3)
        # Xpath for searching in employee name
        xpath_for_searching_emp_name = '//label[text()="Employee Name"]/following::div[2]/div/input'
        emp_name_search = driver.find_element(By.XPATH, xpath_for_searching_emp_name)
        # Sending keys for searching in employee name
        emp_name_search.send_keys("Ricky Thomas Hughes")
        time.sleep(3)
        # Xpath for clicking on Search button
        xpath_for_clicking_on_search = '//button[@type="submit"]'
        search_click = driver.find_element(By.XPATH, xpath_for_clicking_on_search)
        # Clicking on Search button       
        search_click.click()
        time.sleep(3)
        # Xpath for clicking on edit button
        xpath_for_edit_button = '//button[@class="oxd-icon-button oxd-table-cell-action-space"][2]'
        click_on_edit_button = driver.find_element(By.XPATH, xpath_for_edit_button)
        # Clicking on edit button       
        click_on_edit_button.click()
        time.sleep(5)
        # Going to job details
        xpath_for_job_details = '//a[text()="Job"]'
        time.sleep(2)       
        job_details_click = driver.find_element(By.XPATH, xpath_for_job_details)
        # Clicking on job details
        job_details_click.click()
        time.sleep(3)
        """In the previous case, once, employee job is terminated, their emp
        name also disapears. Hence unable to activate it but the below code is the correct xpath 
        for it"""    
        # Xpath for clicking on activate employment
        xpath_for_activate_emp = "//h6[normalize-space()='Activate Employment']"
        activate_emp = driver.find_element(By.XPATH, xpath_for_activate_emp)
        # Clicking on activate employment
        activate_emp.click()
        time.sleep(3)
        # Xpath for terminate employment
        xpath_for_terminate_employment = "//button[normalize-space()='Terminate Employment']"
        terminate_employment = driver.find_element(By.XPATH, xpath_for_terminate_employment)
        print("Employee job is activated")
        time.sleep(3)
        driver.quit()
abc = job_details()
abc.test()




