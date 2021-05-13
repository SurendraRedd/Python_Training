from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

def test_amazon():
  driver = webdriver.Chrome(ChromeDriverManager().install())
  # get method to launch the URL
  driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
  driver.maximize_window()
  Title = driver.title
  driver.find_element_by_id("ap_email").send_keys("hsrinivas79@gmail.com")
  driver.find_element_by_id("continue").click()
  driver.find_element_by_id("ap_password").send_keys("Amazon@123")
  driver.find_element_by_id("signInSubmit").click()
  driver.implicitly_wait(5)
  d = ActionChains(driver)
  a = driver.find_element_by_xpath("//*[@id='nav-link-accountList']/span[1]")
  d.move_to_element(a).perform()
  v=driver.find_elements_by_xpath("//*[@id='nav-flyout-accountList']")
  for i in v :
    print(i.text)
    if "Discover" in  i.text :
      print("Reached inside loop")
      a = driver.find_element_by_xpath("//*[@id='nav-link-accountList']/span[1]")
      d.move_to_element(a).perform()
      secondLevelMenu = driver.find_element_by_xpath('//*[@id="nav-al-wishlist"]/a[5]/span')
      secondLevelMenu.click()
      driver.implicitly_wait(5)
      assert driver.current_url == 'https://www.amazon.in/discover/?ref_=nav_ListFlyout_sbl'
      print('Clicked the required url')    
  driver.close()

