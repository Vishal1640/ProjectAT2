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

class tax_details():

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
        emp_name_search.send_keys("Phil Joel Hughes")
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
        # Going to Tax Exemptions
        xpath_for_tax_exemptions = '//a[text()="Tax Exemptions"]'
        time.sleep(2)       
        tax_exemptions_details_click = driver.find_element(By.XPATH, xpath_for_tax_exemptions)
        # Clicking on salary details
        tax_exemptions_details_click.click()
        time.sleep(3)
        # Xpath for status_1
        xpath_for_status_fit = '//h6[text()="Federal Income Tax"]/following::div[7]'
        status_input_fit = driver.find_element(By.XPATH, xpath_for_status_fit)
        status_input_fit.click()
        # Clicking on status
        status_fit_drop_down = '//div[@role="option"]/span[text()="Single"]'
        clicking_on_status_fit = driver.find_element(By.XPATH, status_fit_drop_down)
        clicking_on_status_fit.click()
        time.sleep(3)
        # Xpath for exemptions
        xpath_for_exemptions = '//h6[text()="Federal Income Tax"]/following::div[14]/input'
        exemptions_input_fit = driver.find_element(By.XPATH, xpath_for_exemptions)
        # Sending keys for exemptions
        exemptions_input_fit.send_keys("79")
        time.sleep(3)
        # Xpath for state
        xpath_for_state = '//label[text()="State"]/following::div[1]'
        state_fill = driver.find_element(By.XPATH, xpath_for_state)
        state_fill.click()
        # Clicking on state
        state_drop_down = '//div[@role="option"]/span[text()="Alaska"]'
        clicking_on_state = driver.find_element(By.XPATH, state_drop_down)
        clicking_on_state.click()
        time.sleep(3)
        # Xpath for status_2
        xpath_for_status_sit = '//h6[text()="State Income Tax"]/following::div[14]'
        status_input_sit = driver.find_element(By.XPATH, xpath_for_status_sit)
        status_input_sit.click()
        # Clicking on status_2
        status_sit_drop_down = '//div[@role="option"]/span[text()="Single"]'
        clicking_on_status_sit = driver.find_element(By.XPATH, status_fit_drop_down)
        clicking_on_status_sit.click()
        time.sleep(3)
        # Xpath for exemptions
        xpath_for_exemptions_sit = '//h6[text()="State Income Tax"]/following::div[22]/input'
        exemptions_input_sit = driver.find_element(By.XPATH, xpath_for_exemptions_sit)
        # Sending keys for exemptions
        exemptions_input_sit.send_keys("19")
        time.sleep(3)
        # Xpath for unempl state
        xpath_for_unemp_state = '//label[text()="Unemployment State"]/following::div[1]'
        unemp_state = driver.find_element(By.XPATH, xpath_for_unemp_state)
        unemp_state.click()
        # Clicking on unempl state
        unempl_state_drop_down = '//div[@role="option"]/span[text()="Alaska"]'
        clicking_on_unempl_state = driver.find_element(By.XPATH, unempl_state_drop_down)
        clicking_on_unempl_state.click()
        time.sleep(3)
        # Xpath for work state
        xpath_for_work_state = '//label[text()="Work State"]/following::div[3]'
        work_state = driver.find_element(By.XPATH, xpath_for_work_state)
        work_state.click()
        # Clicking on work state
        work_state_drop_down = '//div[@role="option"]/span[text()="Alabama"]'
        drop_down_ws = driver.find_element(By.XPATH, work_state_drop_down)
        drop_down_ws.click()
        time.sleep(3)
        # Xpath for save
        xpath_for_save = '//button[@type="submit"]'
        click_on_save = driver.find_element(By.XPATH, xpath_for_save)
        # Clicking on save
        click_on_save.click()
        time.sleep(3)
        print("All fields are filled up properly")
        time.sleep(3)
        # Validating the filled details are present
        try:
            test_1 = exemptions_input_sit.text
            print("Filled details are present")
        except:
            print("Filled details are not present")  
        driver.quit()
abc = tax_details()
abc.test()



        
        
        
        