from selenium.webdriver.common.by import By
 
class Login:
    def __init__(self, driver):
        self.driver = driver
 
        self.email = "tomsmith"
        self.password = "SuperSecretPassword!"
        self.password1 = "SuperSecretPassword"
 
        self.username_locator = "username"
        self.password_locator = "password"
  
        # 3 classes chained together, which we will use via a CSS selector
        self.login_button = ".fa.fa-2x.fa-sign-in"        
 
    def validlogin(self):
        self.driver.find_element(By.ID, self.username_locator).send_keys(self.email)
        self.driver.find_element(By.ID, self.password_locator).send_keys(self.password)
        self.driver.find_element(By.CSS_SELECTOR, self.login_button).click()
    
    def invalidlogin(self):
        self.driver.find_element(By.ID, self.username_locator).send_keys(self.email)
        self.driver.find_element(By.ID, self.password_locator).send_keys(self.password1)
        self.driver.find_element(By.CSS_SELECTOR, self.login_button).click()