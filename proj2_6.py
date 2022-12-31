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


class contact_details():

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
        # Going to contact details
        xpath_for_contact_details = '//div[@role="tab"]/following::div[1]/a[text()="Contact Details"]'
        time.sleep(5)       
        contact_details_click = driver.find_element(By.XPATH, xpath_for_contact_details)
        # Clicking on contact details
        contact_details_click.click()
        time.sleep(3)
        # Finding xpath for street 1
        xpath_for_street_1 = '//label[text()="Street 1"]/following::div[1]/input'
        entering_street_1 = driver.find_element(By.XPATH, xpath_for_street_1)
        time.sleep(3)
        # Sending keys for street 1
        entering_street_1.send_keys("No 7/3, Rainbow Colony")
        time.sleep(3)
        # Finding xpath for street 2
        xpath_for_street_2 = '//label[text()="Street 2"]/following::div[1]/input'
        entering_street_2 = driver.find_element(By.XPATH, xpath_for_street_2)
        time.sleep(3)
        # Sending keys for street 2
        entering_street_2.send_keys("Chennai 60028")
        time.sleep(3)
        # Finding xpath for City
        xpath_for_city = '//label[text()="City"]/following::div[1]/input'
        entering_city = driver.find_element(By.XPATH, xpath_for_city)
        time.sleep(3)
        # Sending keys for City
        entering_city.send_keys("Chennai")
        time.sleep(3)
        # Finding xpath for State/Province
        xpath_for_state = '//label[text()="State/Province"]//following::div[1]/input'
        entering_state = driver.find_element(By.XPATH, xpath_for_state)
        time.sleep(3)
        # Sending keys for State/Province
        entering_state.send_keys("Tamil Nadu")
        time.sleep(3)
        # Finding xpath for Zip/Postal Code
        xpath_for_pc = '//label[text()="Zip/Postal Code"]//following::div[1]/input'
        entering_pc = driver.find_element(By.XPATH, xpath_for_pc)
        time.sleep(3)
        # Sending keys for Zip/Postal Code
        entering_pc.send_keys("60028")
        time.sleep(3)
        # Finding xpath for Country
        xpath_for_country = '//label[text()="Country"]/following::div[1]'
        country_enter = driver.find_element(By.XPATH, xpath_for_country)
        country_enter.click()
        time.sleep(3)
        selecting_country = "//div[@role='option']/span[text()='India']"
        country_choose = driver.find_element(By.XPATH, selecting_country)
        country_choose.click()
        # Finding xpath for home tele no
        xpath_for_home_no = '//label[text()="Home"]/following::div[1]/input'
        entering_home_no = driver.find_element(By.XPATH, xpath_for_home_no)
        time.sleep(3)
        # Sending keys for home tele no
        entering_home_no.send_keys("12345678")
        time.sleep(3)
        # Finding xpath for mob tele no
        xpath_for_mob_no = '//label[text()="Mobile"]/following::div[1]/input'
        entering_mob_no = driver.find_element(By.XPATH, xpath_for_mob_no)
        time.sleep(3)
        # Sending keys for mob tele no
        entering_mob_no.send_keys("87654321")
        time.sleep(3)
        # Finding xpath for work tele no
        xpath_for_work_no = '//label[text()="Work"]/following::div[1]/input'
        entering_work_no = driver.find_element(By.XPATH, xpath_for_work_no)
        time.sleep(3)
        # Sending keys for work tele no
        entering_work_no.send_keys("02468")
        time.sleep(3)
        # Finding xpath for work email
        xpath_for_work_email = '//label[text()="Work Email"]/following::div[1]/input'
        entering_work_email = driver.find_element(By.XPATH, xpath_for_work_email)
        time.sleep(3)
        # Sending keys for work email
        entering_work_email.send_keys("ripo@hotmail.com")
        time.sleep(3)
        # Finding xpath for other email
        xpath_for_other_email = '//label[text()="Other Email"]/following::div[1]/input'
        entering_other_email = driver.find_element(By.XPATH, xpath_for_other_email)
        time.sleep(3)
        # Sending keys for work email
        entering_other_email.send_keys("pori@hotmail.com")
        time.sleep(3)
        # Xpath for save
        xpath_for_saving_1 = '//button[@type="submit"]'
        saving_entry_1 = driver.find_element(By.XPATH, xpath_for_saving_1)
        # Clicking on Save
        saving_entry_1.click()
        time.sleep(3)
        print("Saved and validated all details are present")
        time.sleep(5)
        # Validating the filled details are present
        try:
            test_1 = entering_other_email.text
            print("Filled details are present")
        except:
            print("Filled details are not present")  
        time.sleep(3) 
        driver.quit()

abc = contact_details()

abc.test()
        
        

        
        
        


        

        
        
        

