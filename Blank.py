import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""SELENIUM BOT FOR AUTOMATING TYPING TEST ON --> 10 FAST FINGERS.COM"""

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe", options=chrome_options)

driver.get("https://10fastfingers.com/")
driver.find_element_by_id("typing-test").click()
driver.find_element_by_link_text("Login / Create Account").click()

EMAIL = "PUT YOUR EMAIL IN HERE ."         # <----
PASSWORD = "PUT YOUR PASSWORD HERE"        # <----

driver.implicitly_wait(4)
driver.find_element_by_id("UserEmail").send_keys(EMAIL)
driver.find_element_by_id("UserPassword").send_keys(PASSWORD)


driver.find_element_by_id("login-form-submit").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@wordnr='0']")))

words = driver.find_elements_by_xpath("//div[@id='row1']/span")

for index in range(len(words)):
    word = driver.find_element_by_xpath(f"//span[@wordnr='{index}']").get_attribute("textContent")
    driver.find_element_by_id("inputfield").send_keys(word)
    driver.find_element_by_id("inputfield").send_keys(" ")
    time.sleep(0.1)  # <--- change this value up or down to increase or decrease typing speed



