from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def open_search_tokped(cari):
    driver = webdriver.Chrome()
    driver.get('https://www.tokopedia.com/')
    search = driver.find_element(By.XPATH, '//input[@type="search" and contains(@class, "css-3017qm") and contains(@class, "exxxdg63")]')
    search.send_keys(cari)
    search.send_keys(Keys.RETURN)
    time.sleep(10)
    return driver
