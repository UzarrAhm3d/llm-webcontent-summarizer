import sys
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from urllib.parse import urlparse
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
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h2"))
            )

            search_results[0].click()
            
            # blacklist = ["wikipedia.org", "britannica.com", "wiktionary.org"]
            # target_url = None

            # for link in search_results:
            #     url = link.get_attribute("href")
            #     domain = urlparse(url).netloc.lower()

            #     if not any(bad in domain for bad in blacklist):
            #         target_url = url
            #         break
        except:
            driver.quit()

        time.sleep(3)

        # about_links = driver.find_element(By.PARTIAL_LINK_TEXT, "About")

        # if about_links:
        #     about_links[0].click()
        # else:
        #     driver.quit()

        try:
            title = driver.find_element(By.ID, "firstHeading").text
            content = driver.find_element(By.ID, "mw-content-text").text

            self.title = title
            self.text = content
        except:
            driver.quit()

        # driver.quit()