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
driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com/")
driver.fullscreen_window()
driver.find_element(By.NAME,"user-name").send_keys("standard_user")
driver.find_element(By.NAME,"password").send_keys("secret_sauce")
driver.find_element(By.NAME,"login-button").click()
driver.find_element(By.XPATH,"//div[normalize-space()='Sauce Labs Backpack']").click()
driver.find_element(By.NAME,"add-to-cart").click()
driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[@id='checkout']").click()
driver.find_element(By.XPATH,"//input[@id='first-name']").send_keys("Diwash")
driver.find_element(By.NAME,"lastName").send_keys("Sharma")
driver.find_element(By.XPATH,"//input[@id='postal-code']").send_keys("44600")
driver.find_element(By.NAME,"continue").click()
driver.find_element(By.NAME,"finish").click()
time.sleep(2)
driver.find_element(By.NAME,"back-to-products").click()
time.sleep(5)