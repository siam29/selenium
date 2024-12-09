from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd
import json
from webdriver_manager.chrome import ChromeDriverManager

# Setup Selenium WebDriver
def setup_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

# Scrape data from the website
def scrape_data():
    # Initialize the driver
    driver = setup_driver()

    # Visit the site
    url = "https://www.alojamiento.io/"
    driver.get(url)
    time.sleep(5)  # Allow time for page to load

    # Retrieve ScriptData from the window object using JavaScript
    try:
        script_data = driver.execute_script("return window.ScriptData")
        if script_data:
            # Extract required values from script_data
            site_url = script_data['config']['SiteUrl']
            site_name = script_data['config']['SiteName']
            campaign_id = script_data['pageData'].get('CampaignId', 'Not found')
            user_info = script_data.get('userInfo', {})
            browser = user_info.get('Browser', 'Not found')
            country_code = user_info.get('CountryCode', 'Not found')
            ip = user_info.get('IP', 'Not found')

            # Prepare data for Excel
            data = {
                'SiteURL': [site_url],
                'CampaignID': [campaign_id],
                'SiteName': [site_name],
                'Browser': [browser],
                'CountryCode': [country_code],
                'IP': [ip]
            }

            # Create DataFrame
            df = pd.DataFrame(data)

            # Save to Excel
            df.to_excel('scraped_data.xlsx', index=False)
            print("Data saved to 'scraped_data.xlsx'")
        else:
            print("Script data is not available!")
    except Exception as e:
        print(f"Error occurred: {e}")

    # Close the driver
    driver.quit()

# Run the scraping function
scrape_data()
