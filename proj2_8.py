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
#Using time.sleep instead of implicit wait so that the step by step executions is visble

class dependency_details():

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
        # Going to dependency details
        xpath_for_dependency_details = '//div[@role="tab"]/following::div[1]/a[text()="Dependents"]'
        time.sleep(5)       
        dependency_details_click = driver.find_element(By.XPATH, xpath_for_dependency_details)
        # Clicking on dependency details
        dependency_details_click.click()
        time.sleep(3)
        # Clicking on add
        xpath_for_add = '//h6[text()="Assigned Dependents"]/following::button[1]'
        clicking_on_add = driver.find_element(By.XPATH, xpath_for_add)
        # Clicking on add
        clicking_on_add.click()
        time.sleep(3)
        # Finding xpath for dependency name
        xpath_for_dependency_name = '//label[text()="Name"]/following::div[1]/input'
        dependency_emergency_name = driver.find_element(By.XPATH, xpath_for_dependency_name)
        time.sleep(3)
        # Sending keys for dependency name
        dependency_emergency_name.send_keys("Vinay")
        time.sleep(3)
        # Xpath for relationship
        xpath_for_relationship = '//label[text()="Relationship"]/following::div[1]'
        relationship_enter = driver.find_element(By.XPATH, xpath_for_relationship)
        relationship_enter.click()
        time.sleep(3)
        selecting_relationship = '//div[@role="option"]/span[text()="Child"]'
        relationship_choose = driver.find_element(By.XPATH, selecting_relationship)
        relationship_choose.click()
        # Xpath for DOB
        xpath_for_dob = '//label[text()="Date of Birth"]/following::div[3]/input'
        dob_entry = driver.find_element(By.XPATH, xpath_for_dob)
        time.sleep(2)
        # Sending keys for DOB
        dob_entry.send_keys("1998-12-19")
        time.sleep(3)
        #Xpath for save
        xpath_for_save = '//button[@type="submit"]'
        click_on_save = driver.find_element(By.XPATH, xpath_for_save)
        print("Saved and validated all details are present")
        time.sleep(5)
        # Validating the filled details are present
        try:
            test_1 = dependency_emergency_name.text
            print("Filled details are present")
        except:
            print("Filled details are not present")  
        time.sleep(3) 
        driver.quit()
        
abc = dependency_details()
abc.test()
        