import time
from selenium import webdriver
from selenium.webdriver import Keys
# from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.flipkart.com/")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Mobiles")
search_box.send_keys(Keys.RETURN)
driver.find_element(By.NAME, "q")

time.sleep(5)

first_product = driver.find_element(By.CSS_SELECTOR, "div._75nlfW")  # it perform actions like  loginpage,
# checking prices , addtocart

first_product.click()
driver.quit()
