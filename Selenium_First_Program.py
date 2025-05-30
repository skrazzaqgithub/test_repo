from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://money.rediff.com/index.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[contains(.,'Trends')]").click()