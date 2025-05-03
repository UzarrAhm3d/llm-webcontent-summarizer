import sys
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class SelenScrap:

    query: str
    title: str
    text: str

    def __init__(self, query):
        
        driver = webdriver.Chrome()
        
        time.sleep(3)

        driver.get("https://duckduckgo.com/")

        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query)

        time.sleep(3)
        search_box.send_keys(Keys.RETURN)

        try:
            search_results = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3"))
            )

            search_results[0].click()

        except:
            driver.quit()

        time.sleep(3)

        about_links = driver.find_element(By.PARTIAL_LINK_TEXT, "About")

        if about_links:
            time.sleep(3)
            about_links[0].click()
        else:
            driver.quit()

        try:
            time.sleep(3)
            content = driver.find_element(By.TAG_NAME, "body").text

            print(content[:1500])
        except:
            driver.quit()

        # driver.quit()