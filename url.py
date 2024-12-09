from selenium.webdriver.common.by import By
import requests

# Test for URL status
def test_url(driver, page_url):
    driver.get(page_url)
    
    # Find all links on the page
    links = driver.find_elements(By.TAG_NAME, "a")
    print(f"Found {len(links)} links on the page.")
    
    url_status_list = []  # List to store the URL status for all links
    
    for link in links:
        url = link.get_attribute("href")
        
        if url:
            try:
                # Send a GET request to check the URL status
                response = requests.get(url, timeout=5)  # Added timeout to prevent hanging requests
                
                # Check if the response status is 404
                if response.status_code == 404:
                    url_status_list.append({
                        "page_url": url,
                        "testcase": "URL Status",
                        "status": "404 Not Found",
                        "comments": "Page not found"
                    })
                else:
                    url_status_list.append({
                        "page_url": url,
                        "testcase": "URL Status",
                        "status": f"{response.status_code} OK",
                        "comments": "Valid URL"
                    })
            except requests.exceptions.RequestException as e:
                url_status_list.append({
                    "page_url": url,
                    "testcase": "URL Status",
                    "status": "Error",
                    "comments": f"Error: {e}"
                })
    
    return url_status_list  # Ensure the function returns the full list of results
