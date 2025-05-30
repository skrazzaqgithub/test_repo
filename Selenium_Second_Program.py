from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://en.wikipedia.org/wiki/Rabindranath_Tagore")
driver.find_element(By.ID,"vector-main-menu-dropdown-checkbox").click()
driver.find_element(By.ID,"p-navigation").click()
# driver.find_element(By.ID,"txtPassword").send_keys("admin123")
# driver.find_element(By.ID,"btnLogin").click()

act_title=driver.title
exp_title="Visit the main page"
if act_title==exp_title:
    print("Test is Passed")
else:
    print("Test is Failed")
driver.close()
# driver.maximize_window()

# driver.find_element(By.XPATH,"//a[contains(.,'Trends')]").click()