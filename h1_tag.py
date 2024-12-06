from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def test_h1_tag_existence(driver, page_url):
    driver.get(page_url)
    try:
        driver.find_element(By.TAG_NAME, "h1")
        return {"page_url": page_url, "testcase": "H1 tag existence", "status": "pass", "comments": "H1 tag exists"}
    except:
        return {"page_url": page_url, "testcase": "H1 tag existence", "status": "fail", "comments": "Missing H1 tag"}