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
        time.sleep(2)
        print("Validation is successfull")
        # Validating below menu options are displaying in Side pane(Negative scenario)
        xpath_for_side_pane_1 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
        side_pane_1 = driver.find_element(By.XPATH, xpath_for_side_pane_1)
        assert side_pane_1, side_pane.is_displayed()
        print("Validation is  not successfull")
        time.sleep(2)
        # Validating Search text box is displaying on Side pane
        xpath_for_search = '//div[@class="oxd-main-menu-search"]'
        search_button = driver.find_element(By.XPATH,xpath_for_search)
        assert search_button, search_button.is_displayed()
        print("Search box is displaying on Admin page")
        # Clicking on search box with provided text
        xpath_for_search = '//input[@placeholder="Search"]'
        searching_on_search = driver.find_element(By.XPATH, xpath_for_search)
        # Using for loop to search in upper
        list_1 = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard", "Directory", "Maintenance", "Buzz"]
        for a in list_1:
            searching_on_search.send_keys(a.upper())
            time.sleep(1)
        # Clearing existing text
            searching_on_search.send_keys(Keys.CONTROL,'a')
            searching_on_search.send_keys(Keys.BACKSPACE)
            time.sleep(1)
        # Using for loop to search in upper
        for a in list_1:
            searching_on_search.send_keys(a.lower())
            time.sleep(1)
        # Clearing existing text
            searching_on_search.send_keys(Keys.CONTROL,'a')
            searching_on_search.send_keys(Keys.BACKSPACE)
            time.sleep(1)
        print("Individual menu are displayed under search box") 
        driver.quit()      
abc = orangehrm()
abc.test()