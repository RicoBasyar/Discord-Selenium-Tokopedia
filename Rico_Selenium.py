from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import asyncio as asyc

def sync_open_search_tokped(cari):
    driver = webdriver.Chrome()
    driver.get('https://www.tokopedia.com/')
    search = driver.find_element(By.XPATH, '//input[@type="search" and contains(@class, "css-3017qm") and contains(@class, "exxxdg63")]')
    search.send_keys(cari)
    search.send_keys(Keys.RETURN)
    time.sleep(10)
    barang_elements = driver.find_elements(By.CLASS_NAME, 'prd_link-product-name')
    harga_elements = driver.find_elements(By.CLASS_NAME, 'prd_link-product-price')

    barang = [x.text for x in barang_elements]
    harga = [y.text for y in harga_elements]

    for x in barang:
        print(x)

    for y in harga:
        print(y)

    return list(zip(barang, harga))

#def sync_get_info_tokped(cari):
    #driver = webdriver.Chrome()
    #search = driver.find_elements(By.CLASS_NAME, 'prd_link-product-name')
    #return print(search)


async def open_search_tokped(cari):
    loop = asyc.get_event_loop()
    return await loop.run_in_executor(None, sync_open_search_tokped, cari)

#async def get_info_tokped(cari):
    #loop = asyc.get_event_loop()
    #return await loop.run_in_executor(None, sync_get_info_tokped, cari)