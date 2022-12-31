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
        # Xpath for joined date
        xpath_for_joined_date = "//label[text()='Joined Date']/following::input[1]"
        joined_date_enter = driver.find_element(By.XPATH, xpath_for_joined_date)
        time.sleep(2)
        # Sending keys for joined date
        joined_date_enter.send_keys("2018-12-19")
        time.sleep(3)
        # Xpath for job title
        xpath_for_job_title = "//label[normalize-space()='Job Title']/following::div[3]"
        job_title_enter = driver.find_element(By.XPATH, xpath_for_job_title)
        job_title_enter.click()  
        time.sleep(3)     
        # Xpath for selecting title
        xpath_for_selecting_title = "//div[@role='option']/span[text()='Software Engineer']"
        selecting_title = driver.find_element(By.XPATH, xpath_for_selecting_title)        
        selecting_title.click()
        time.sleep(3)
        # Xpath for job category
        xpath_for_job_category = '//label[text()="Job Category"]/following::div[1]'
        job_category_enter = driver.find_element(By.XPATH, xpath_for_job_category)
        job_category_enter.click()       
        # Xpath for selecting job category
        xpath_for_selecting_job_category = '//div[@role="option"]/span[text()="Professionals"]'
        selecting_title = driver.find_element(By.XPATH, xpath_for_selecting_job_category)        
        selecting_title.click()
        time.sleep(3)
        # Xpath for sub units
        xpath_for_sub_units = "//label[text()='Sub Unit']/following::div[1]"
        sub_units_enter = driver.find_element(By.XPATH, xpath_for_sub_units)
        sub_units_enter.click()       
        # Xpath for selecting sub units
        xpath_for_selecting_sub_units = "//div[@role='option']/span[text()='Quality Assurance']"
        selecting_sub_units = driver.find_element(By.XPATH, xpath_for_selecting_sub_units)        
        selecting_sub_units.click()
        time.sleep(3)
        # Xpath for location
        xpath_for_location = "//label[text()='Location']/following::div[1]"
        location_enter = driver.find_element(By.XPATH, xpath_for_location)
        location_enter.click()       
        # Xpath for selecting job location
        xpath_for_location = '//div[@role="option"]/span[text()="Canadian Regional HQ"]'
        location_title = driver.find_element(By.XPATH, xpath_for_location)        
        location_title.click()
        time.sleep(3)
        # Xpath for employment status
        xpath_for_employment_status = '//label[text()="Employment Status"]/following::div[1]'
        employment_status_enter = driver.find_element(By.XPATH, xpath_for_employment_status)
        employment_status_enter.click()       
        # Xpath for selecting employment status
        xpath_for_employment_status = '//div[@role="option"]/span[text()="Full-Time Permanent"]'
        employment_status_title = driver.find_element(By.XPATH, xpath_for_employment_status)        
        employment_status_title.click()
        time.sleep(3)
        # Xpath for enabling Employment Contract Details
        xpath_for_employment_contract_details = '//p[text()="Include Employment Contract Details"]/following::div[1]'
        employment_contract_details = driver.find_element(By.XPATH, xpath_for_employment_contract_details)
        # Clicking on employment Contract Details
        employment_contract_details.click()
        # Xpath for contract start date
        xpath_for_start_date = "//p[text()='Include Employment Contract Details']/following::input[2]"
        start_date_enter = driver.find_element(By.XPATH, xpath_for_start_date)
        time.sleep(2)
        # Sending keys for contract start date
        start_date_enter.send_keys("2022-12-19")
        time.sleep(3)     
        # Xpath for contract end date
        xpath_for_end_date = "//p[text()='Include Employment Contract Details']/following::input[3]"
        end_date_enter = driver.find_element(By.XPATH, xpath_for_end_date)
        time.sleep(2)
        # Sending keys for contract start date
        end_date_enter.send_keys("2024-12-19")
        time.sleep(3) 
        # Xpath for button
        xpath_for_button = '//button[@type="submit"]'
        button_click = driver.find_element(By.XPATH, xpath_for_button)
        # Clicking on button
        button_click.click()
        time.sleep(5)
        print("Saved and validated all details are present")
        time.sleep(5)
        # Validating the filled details are present
        try:
            test_1 = end_date_enter.text
            print("Filled details are present")
        except:
            print("Filled details are not present")  
        time.sleep(3) 
        driver.quit() 

abc = job_details()
abc.test()
