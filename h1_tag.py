from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def test_h1_tag_existence(driver, page_url):
    h1_list=[]
    driver.get(page_url)
    try:
        driver.find_element(By.TAG_NAME, "h1")
        h1_list.append( {"page_url": page_url, "testcase": "H1 tag existence", "status": "pass", "comments": "H1 tag exists"})
    except:
        h1_list.append( {"page_url": page_url, "testcase": "H1 tag existence", "status": "fail", "comments": "Missing H1 tag"})

    return h1_list
    

