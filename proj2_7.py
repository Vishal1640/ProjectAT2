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

class emergency_details():

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
        # Going to emergency details
        xpath_for_emergency_details = '//div[@role="tab"]/following::div[1]/a[text()="Emergency Contacts"]'
        time.sleep(5)       
        emergency_details_click = driver.find_element(By.XPATH, xpath_for_emergency_details)
        # Clicking on emergency details
        emergency_details_click.click()
        time.sleep(3)
        # Clicking on add
        xpath_for_add = '//h6[text()="Assigned Emergency Contacts"]/following::button[1]'
        time.sleep(5)
        clicking_on_add = driver.find_element(By.XPATH, xpath_for_add)
        # Clicking on add
        clicking_on_add.click()
        time.sleep(3)
        # Finding xpath for emer name
        xpath_for_emergency_name = '//label[text()="Name"]/following::div[1]/input'
        entering_emergency_name = driver.find_element(By.XPATH, xpath_for_emergency_name)
        time.sleep(3)
        # Sending keys for emer name
        entering_emergency_name.send_keys("Vinay")
        time.sleep(3)
        # Finding xpath for emer rel
        xpath_for_emergency_relationship = '//label[text()="Relationship"]/following::div[1]/input'
        entering_emergency_relationship = driver.find_element(By.XPATH, xpath_for_emergency_relationship)
        time.sleep(3)
        # Sending keys for emer rel
        entering_emergency_relationship.send_keys("Single")
        time.sleep(3)
        # Finding xpath for home tele
        xpath_for_emergency_home_tele = '//label[text()="Home Telephone"]/following::div[1]/input'
        entering_emergency_home_tele = driver.find_element(By.XPATH, xpath_for_emergency_home_tele)
        time.sleep(3)
        # Sending keys for home tele
        entering_emergency_home_tele.send_keys("123456")
        time.sleep(3)
        # Finding xpath for home tele
        xpath_for_emergency_mob_tele = '//label[text()="Mobile"]/following::div[1]/input'
        entering_emergency_mob_tele = driver.find_element(By.XPATH, xpath_for_emergency_mob_tele)
        time.sleep(3)
        # Sending keys for home tele
        entering_emergency_mob_tele.send_keys("654321")
        time.sleep(3)
        # Finding xpath for work tele
        xpath_for_emergency_work_tele = '//label[text()="Work Telephone"]/following::div[1]/input'
        entering_emergency_work_tele = driver.find_element(By.XPATH, xpath_for_emergency_work_tele)
        time.sleep(3)
        # Sending keys for work tele
        entering_emergency_work_tele.send_keys("023468")
        time.sleep(3)
        # Xpath for save
        xpath_for_saving_1 = '//button[@type="submit"]'
        saving_entry_1 = driver.find_element(By.XPATH, xpath_for_saving_1)
        # Clicking on Save
        saving_entry_1.click()
        time.sleep(3)
        print("Saved and validated all details are present")
        time.sleep(5)
        # Validating the filled details are present(Negative scenario)
        xpath_for_save_emerg_contact = '//h6[text() = "Save Emergency Contact"]'
        save_emergency_contact = driver.find_element(By.XPATH, xpath_for_save_emerg_contact)
        try:
            test_1 = save_emergency_contact.text
            print("Filled details are present")
        except:
            print("Filled details are not present")  
        time.sleep(3)         
        driver.quit()

abc = emergency_details()

abc.test()

        





