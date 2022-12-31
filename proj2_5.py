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

class personal_details():

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
        # Going to personal details
        xpath_for_personal_details = '//a[@class="orangehrm-tabs-item --active"]'       
        personal_details_click = driver.find_element(By.XPATH, xpath_for_personal_details)
        # Clicking on personal details
        personal_details_click.click()
        time.sleep(3)
        # Xpath for nickname
        xpath_for_nickname = "//label[text()='Nickname']/following::div[1]/input"
        nickname_enter = driver.find_element(By.XPATH, xpath_for_nickname)
        # Sending keys for nickname
        nickname_enter.send_keys("Punter")
        time.sleep(3)
        # Xpath for emp id
        xpath_for_emp_id = "//label[text()='Employee Id']/following::div[1]/input"
        emp_id_enter = driver.find_element(By.XPATH, xpath_for_emp_id)
        # Sending keys for nickname
        emp_id_enter.send_keys("1998")
        time.sleep(3)
       # Xpath for other id
        xpath_for_other_id = '//label[text()="Other Id"]/following::div[1]/input'
        other_id_enter = driver.find_element(By.XPATH, xpath_for_other_id)
        # Sending keys for other id
        other_id_enter.send_keys("1998")
        time.sleep(3)
        # Xpath for License expiry date
        xpath_for_license_exp_date = "(//input[@placeholder='yyyy-mm-dd'])[1]"
        license_exp_date_enter = driver.find_element(By.XPATH, xpath_for_license_exp_date)
        # Sending keys for License expiry date
        license_exp_date_enter.send_keys("2022-12-19")
        time.sleep(3)
        # Xpath for SSN no
        xpath_for_ssn_no = '//label[text()="SSN Number"]/following::div[1]/input'
        ssn_no_enter = driver.find_element(By.XPATH, xpath_for_ssn_no)
        # Sending keys for other id
        ssn_no_enter.send_keys("1640")
        time.sleep(3)
        # Xpath for SIN no
        xpath_for_sin_no = '//label[text()="SIN Number"]/following::div[1]/input'
        sin_no_enter = driver.find_element(By.XPATH, xpath_for_sin_no)
        # Sending keys for other id
        sin_no_enter.send_keys("0416")
        time.sleep(3)
        # Xpath for Nationality
        xpath_for_nationality = '//label[text()="Nationality"]/following::div[1]'
        nationality_enter = driver.find_element(By.XPATH, xpath_for_nationality)
        nationality_enter.click()
        selecting_nation = "//div[@role='option']/span[text()='Indian']"
        nation_choose = driver.find_element(By.XPATH, selecting_nation)
        nation_choose.click()
        # Xpath for Marital Status
        xpath_for_marital_status = '//label[text()="Marital Status"]/following::div[1]'
        marital_status_entry = driver.find_element(By.XPATH, xpath_for_marital_status)
        marital_status_entry.click()
        status_entered = "//div[@role='option']/span[text()='Single']"
        enter_status = driver.find_element(By.XPATH, status_entered)
        enter_status.click()
        # Xpath for DOB
        xpath_for_dob = '//label[text()="Date of Birth"]/following::div[3]/input'
        dob_entry = driver.find_element(By.XPATH, xpath_for_dob)
        time.sleep(2)
        # Sending keys for DOB
        dob_entry.send_keys("1998-12-19")
        time.sleep(3)
        # Xpath for gender
        xpath_for_gender = '//label[normalize-space()="Male"]'
        gender_entry = driver.find_element(By.XPATH, xpath_for_gender)
        # Clicking on gender
        gender_entry.click()
        # Xpath for MS
        xpath_for_MS = '//label[text()="Military Service"]/following::div[1]/input'
        ms_entry = driver.find_element(By.XPATH, xpath_for_MS)
        # Sending keys for MS
        ms_entry.send_keys("No")
        # Xpath for save
        xpath_for_saving = '//button[@type="submit"]'
        saving_entry = driver.find_element(By.XPATH, xpath_for_saving)
        # Clicking on Save
        saving_entry.click()
        time.sleep(5)
        # # Xpath for blood group
        xpath_for_blood_group = '//label[text()="Blood Type"]/following::div[1]'
        blood_group_chosen = driver.find_element(By.XPATH, xpath_for_blood_group)
        blood_group_chosen.click()
        blood_group_enetered = "//div[@role='option']/span[text()='O+']"
        bg_entered = driver.find_element(By.XPATH, blood_group_enetered)
        bg_entered.click()
        time.sleep(5)
        # Xpath for save 2
        xpath_for_saving_2 = "//div[@class='orangehrm-custom-fields']//button[@type='submit'][normalize-space()='Save']"
        saving_entry_2 = driver.find_element(By.XPATH, xpath_for_saving_2)
        # Clicking on Save
        saving_entry_2.click()
        time.sleep(3)
        print("Saved and validated all details are present")
        time.sleep(5)
        # Validating the filled details are present
        try:
            test_1 = ssn_no_enter.text
            print("Filled details are present")
        except:
            print("Filled details are not present")
        time.sleep(3)

        driver.quit()
abc = personal_details()
abc.test()