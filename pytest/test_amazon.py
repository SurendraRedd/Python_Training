from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

def test_amazon():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #driver = webdriver.Chrome(executable_path =r'C:/pytest_selenium/chromedriver_win32/chromedriver.exe')
    driver.get("https://www.amazon.in/") 
    action = ActionChains(driver)
    firstLevelMenu = driver.find_element_by_xpath('//*[@id="nav-link-accountList-nav-line-1"]')
    action.move_to_element(firstLevelMenu).perform()
    #secondLevelMenu = driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span')
    secondLevelMenu = driver.find_element_by_xpath('//*[@id="nav-al-wishlist"]/a[5]/span')
    secondLevelMenu.click()
    assert driver.current_url == 'https://www.amazon.in/discover/?ref_=nav_ListFlyout_sbl'

    #Select class for dropdown
    l= driver.find_element_by_xpath("//select[@id='searchDropdownBox']")
    d= Select(l)
    print('Options are: ')
    #iterate over dropdown options
    for opt in d.options:
        #get option text
        print(opt.text)
    s = Select(driver.find_element_by_xpath("//select[@id='searchDropdownBox']"))
    #select by option index
    s.select_by_index(4)
    #get selected item with method first_selected_option
    o= s.first_selected_option
    #text method for selected option text
    print("Selected option is: "+ o.text)

    driver.close()