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

class salary_details():

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
        first_name.send_keys("Phil")
        time.sleep(3)
        # Sending input for middle name
        xpath_for_middle_name = '//input[@name="middleName"]'
        middle_name = driver.find_element(By.XPATH, xpath_for_middle_name)
        # Sending keys for middle name
        middle_name.send_keys("Joel")
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
        username_input.send_keys("Ten Doeschate")
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
        # # Xpath for searching in employee name
        # xpath_for_searching_emp_name = '//label[text()="Employee Name"]/following::div[2]/div/input'
        # emp_name_search = driver.find_element(By.XPATH, xpath_for_searching_emp_name)
        # # Sending keys for searching in employee name
        # emp_name_search.send_keys("Ricky Thomas Hughes")
        # time.sleep(3)
        # # Xpath for clicking on Search button
        # xpath_for_clicking_on_search = '//button[@type="submit"]'
        # search_click = driver.find_element(By.XPATH, xpath_for_clicking_on_search)
        # # Clicking on Search button       
        # search_click.click()
        # time.sleep(3)
        # # Xpath for clicking on edit button
        # xpath_for_edit_button = '//button[@class="oxd-icon-button oxd-table-cell-action-space"][2]'
        # click_on_edit_button = driver.find_element(By.XPATH, xpath_for_edit_button)
        # # Clicking on edit button       
        # click_on_edit_button.click()
        # time.sleep(5)
        # Going to salary details
        xpath_for_salary_details = '//a[text()="Salary"]'
        time.sleep(2)       
        salary_details_click = driver.find_element(By.XPATH, xpath_for_salary_details)
        # Clicking on salary details
        salary_details_click.click()
        time.sleep(3)
        # Xpath for clicking on add
        xpath_for_clicking_on_add = "//h6[text()='Assigned Salary Components']/following::i[1]"
        clicking_on_add = driver.find_element(By.XPATH, xpath_for_clicking_on_add)
        # Clicking on add
        clicking_on_add.click()
        time.sleep(3)
        # Xpath for salary comp
        xpath_for_salary_comp = '//label[text()="Salary Component"]/following::div[1]/input'
        filling_on_salary_comp = driver.find_element(By.XPATH, xpath_for_salary_comp)
        # Sending keys for salary comp
        filling_on_salary_comp.send_keys("CTC")
        time.sleep(3)
        # Xpath for Pay grade
        xpath_for_pay_grade = '//label[text()="Pay Grade"]/following::div[1]/div'
        pay_grade = driver.find_element(By.XPATH, xpath_for_pay_grade)
        pay_grade.click()
        # Clicking on Pay grade
        pay_grade_drop_down = '//div[@role="option"]/span[text()="Grade 3"]'
        clicking_on_pay_grade = driver.find_element(By.XPATH, pay_grade_drop_down)
        clicking_on_pay_grade.click()
        time.sleep(3)
        # Xpath for Pay Frequency
        xpath_for_pay_frequency = "//label[text()='Pay Frequency']/following::div[1]/div"
        pay_frequency = driver.find_element(By.XPATH, xpath_for_pay_frequency)
        pay_frequency.click()
        # Clicking on Pay Frequency
        pay_frequency_drop_down = '//div[@role="option"]/span[text()="Monthly"]'
        clicking_on_pay_frequency= driver.find_element(By.XPATH, pay_frequency_drop_down)
        clicking_on_pay_frequency.click()
        time.sleep(3)
        # Xpath for Currency
        xpath_for_currency = "//label[text()='Currency']/following::div[1]"
        currency_frequency = driver.find_element(By.XPATH, xpath_for_currency)
        currency_frequency.click()
        # Clicking on Currency
        currency_drop_down = '//div[@role="option"]/span[text()="United States Dollar"]'
        clicking_on_currency= driver.find_element(By.XPATH, currency_drop_down)
        clicking_on_currency.click()
        time.sleep(3)
        # Xpath for amount
        xpath_for_amt = '//label[text()="Amount"]/following::div[1]/input'
        filling_on_amt = driver.find_element(By.XPATH, xpath_for_amt)
        # Sending keys for salary comp
        filling_on_amt.send_keys("40000")
        time.sleep(3)
        # # Xpath for comments
        # xpath_for_comments = '//label[text()="Comments"]/following::div[1]'
        # filling_on_comments = driver.find_element(By.XPATH, xpath_for_comments)
        # # Sending keys for comments
        # filling_on_comments.send_keys("Done")
        # time.sleep(3)
        # Xpath for clicking on Direct Deposit Details
        xpath_for_ddd = '//p[text()="Include Direct Deposit Details"]/following::div[1]'
        clicking_on_ddd = driver.find_element(By.XPATH, xpath_for_ddd)
        # Clicking on DDD
        clicking_on_ddd.click()
        time.sleep(3)
        # Xpath for Account Number
        xpath_for_acc_no = '//label[text()="Account Number"]/following::div[1]/input'
        filling_on_acc_no = driver.find_element(By.XPATH, xpath_for_acc_no)
        # Sending keys on Account Number
        filling_on_acc_no.send_keys("23456789")
        time.sleep(3)
        # Xpath for Account type
        xpath_for_acc_type = '//label[text()="Account Type"]/following::div[1]'
        acc_type = driver.find_element(By.XPATH, xpath_for_acc_type)
        acc_type.click()
        # Clicking on Account type
        acc_type_drop_down = '//div[@role="option"]/span[text() = "Savings"]'
        clicking_on_acc_type= driver.find_element(By.XPATH, acc_type_drop_down)
        clicking_on_acc_type.click()
        time.sleep(3)
        # Xpath for Routing Number
        xpath_for_routing_no = '//label[text()="Routing Number"]/following::div[1]/input'
        filling_routing_no = driver.find_element(By.XPATH, xpath_for_routing_no)
        # Sending keys on Routing Number
        filling_routing_no.send_keys("26009595")
        time.sleep(3)
        # Xpath for amount # Doubt
        xpath_for_amt_2 = '//p[text()="Include Direct Deposit Details"]/following::div//label[text()="Amount"]/following::div[1]/input'
        amt_2_routing_no = driver.find_element(By.XPATH, xpath_for_amt_2)
        # Sending keys on amount
        amt_2_routing_no.send_keys("30000")
        time.sleep(3)
        # Xpath for save
        xpath_for_save = '//button[@type="submit"]'
        click_on_save = driver.find_element(By.XPATH, xpath_for_save)
        # Clicking on save
        click_on_save.click()
        time.sleep(3)
        print("All fields are filled up properly")
        time.sleep(3)
        # Validating the filled details are present(Negative scenario)
        xpath_for_add_salary_comp = '//h6[text()=" Add Salary Component "]'
        add_salary_comp = driver.find_element(By.XPATH, xpath_for_add_salary_comp)

        try:
            test_1 = add_salary_comp.text
            print("Filled details are present")
        except:
            print("Filled details are not present")  
        driver.quit()
        time.sleep(3) 
abc = salary_details()
abc.test()        
        


        