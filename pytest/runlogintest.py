from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from loginpage import *

def setup():
    return webdriver.Chrome(ChromeDriverManager().install())

def test_validlogin():
    driver = setup() 
    driver.get("https://the-internet.herokuapp.com/login")
 
    login_form = Login(driver)
    login_form.validlogin()
    driver.close()
    driver.quit()

def test_invalidlogin():
    driver = setup() 
    driver.get("https://the-internet.herokuapp.com/login")
 
    login_form = Login(driver)
    login_form.invalidlogin()
    value = driver.find_element_by_xpath('//*[@id="flash"]').text    
    assert value.rstrip("\n") == 'Your password is invalid!\n×'
    driver.close()
    driver.quit()
