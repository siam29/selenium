from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def test_image(driver, page_url):
    image_list=[]
    driver.get(page_url)
    images = driver.find_elements(By.TAG_NAME, "img")
    for img in images:
        alt_attribute = img.get_attribute("alt")
        if not alt_attribute:
            image_list.append( {"page_url": page_url, "testcase": "Image alt attribute", "status": "fail", "comments": "Missing alt attribute for an image"})
    image_list.append( {"page_url": page_url, "testcase": "Image alt attribute", "status": "pass", "comments": "All images have alt attributes"})

    return image_list
