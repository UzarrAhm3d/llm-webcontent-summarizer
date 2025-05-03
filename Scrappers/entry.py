import sys
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from urllib.parse import urlparse
import time

class Entry:

    url: str
    username: str
    password: str

    def __init__(self, url, username, password):
        
        driver = webdriver.Chrome()
        
        time.sleep(3)

        driver.get(url)

        email_input_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "email"))
        )
        password_input_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )

        email_input_box.send_keys(username)
        password_input_box.send_keys(password)

        remember_checkbox = driver.find_element(By.NAME, "remember")

        if remember_checkbox.is_selected():
            remember_checkbox.click()
        
        password_input_box.send_keys(Keys.RETURN)
        
        driver.quit()
        
        print("Operation Successful!")

    