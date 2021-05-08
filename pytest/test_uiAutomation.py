from selenium import webdriver

#driver = webdriver.Chrome(executable_path=r'C:\\pytest_selenium\\chromedriver_win32\\chromedriver.exe')
# driver = webdriver.Chrome(executable_path=r'C:/pytest_selenium/chromedriver_win32/chromedriver.exe')

# driver.implicitly_wait(10)
# driver.maximize_window()

# driver.get('https://opensource-demo.orangehrmlive.com/')
# driver.find_element_by_id("txtUsername").send_keys('Admin')
# driver.find_element_by_id("txtPassword").send_keys('admin123')
# driver.find_element_by_id("btnLogin").click()

# print(driver.title)

# driver.close()
# driver.quit()

# print("Ui test automation using selenium")



# import pytest

# driver = webdriver.Chrome(executable_path=r'C:/pytest_selenium/chromedriver_win32/chromedriver.exe')

# # Prerequisite
# def test_setup():
#     #global driver    
#     driver.implicitly_wait(10)
#     driver.maximize_window()

# def test_loginValidation():    
#     driver.get('https://opensource-demo.orangehrmlive.com/')
#     driver.find_element_by_id("txtUsername").send_keys('Admin')
#     driver.find_element_by_id("txtPassword").send_keys('admin123')
#     driver.find_element_by_id("btnLogin").click()
#     assert driver.title == 'OrangeHRM', 'Test Failed'

# def test_teardown():
#     driver.close()
#     driver.quit()


import pytest
import allure
from pytest_html_reporter import attach

# Decorator 
@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path=r'C:/pytest_selenium/chromedriver_win32/chromedriver.exe')
    driver.implicitly_wait(10)
    driver.maximize_window()
    # Tear down
    yield
    driver.close()
    driver.quit()

@allure.description("Write the test case description --> Checking valid login")
@allure.severity(severity_level="CRITICAL")
# Function calling another function
def test_loginValidation(test_setup):
    driver.get('https://opensource-demo.orangehrmlive.com/')
    log("Navigated to the url")
    driver.find_element_by_id("txtUsername").clear()
    #driver.find_element_by_id("txtUsername").send_keys('Admin')
    enter_username('Admin') 
    log("Entered the username in the website") 
    driver.find_element_by_id("txtPassword").clear()
    #driver.find_element_by_id("txtPassword").send_keys('admin123')
    enter_password('admin123')
    driver.find_element_by_id("btnLogin").click()
    assert driver.title == "OrangeHRM"
    assert "dashboard" in driver.current_url
    log("Completed") 

@allure.description("Validates the login - failcase")
@allure.severity(severity_level="NORMAL")
def test_invalidlogin(test_setup):
    driver.get('https://opensource-demo.orangehrmlive.com/')
    log("Navigated to the url")
    driver.find_element_by_id("txtUsername").clear()
    enter_username('Admin')
    #driver.find_element_by_id("txtUsername").send_keys('Admin')
    driver.find_element_by_id("txtPassword").clear()
    driver.find_element_by_id("txtPassword").send_keys('admin1234')
    enter_password('admin1234')
    driver.find_element_by_id("btnLogin").click()
    value = driver.find_element_by_xpath('//*[@id="spanMessage"]').text
    assert value == 'Invalid credentials'
    #allure.attach(driver.get_screenshot_as_png(),name='InvalidLogin',attachment_type=allure.attachment_type.PNG)    
    attach(data=driver.get_screenshot_as_png())
    log("Completed") 

@allure.step("Enter username as {0}")
def enter_username(username):
    driver.find_element_by_id("txtUsername").send_keys(username)

@allure.step("Enter password as {0}")
def enter_password(password):
    driver.find_element_by_id("txtPassword").send_keys(password)

@allure.step("{0}")
def log(message):
    print(message)