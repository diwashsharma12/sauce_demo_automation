from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
options = webdriver.ChromeOptions()

prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
}

options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
driver.fullscreen_window()
driver.find_element(By.NAME,"user-name").send_keys("standard_user")
driver.find_element(By.NAME,"password").send_keys("secret_sauce")
driver.find_element(By.NAME,"login-button").click()
driver.find_element(By.XPATH,"//div[normalize-space()='Sauce Labs Backpack']").click()
time.sleep(5)
