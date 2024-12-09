from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def test_currency_filter(driver, page_url):
    driver.get(page_url)
    try:
        # Wait until the body is fully loaded
        WebDriverWait(driver, 20).until(
            lambda driver: driver.find_element(By.TAG_NAME, "body")
        )

        # Debug: print page source to check if the elements are present
        print(driver.page_source)

        # Wait for the initial price element to be visible
        initial_price_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "property-tile-price"))
        )
        initial_price = initial_price_element.text
        print(f"Initial Price: {initial_price}")

        # Find and click the currency filter
        currency_filter = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "currency-selector"))
        )
        currency_filter.click()
        print("Currency selector clicked.")

        # Wait for the USD option and select it
        usd_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//option[text()='USD']"))
        )
        usd_option.click()
        print("USD option selected.")

        # Wait for the price to update
        updated_price_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "property-tile-price"))
        )
        updated_price = updated_price_element.text
        print(f"Updated Price: {updated_price}")

        if initial_price != updated_price:
            return {
                "page_url": page_url,
                "testcase": "Currency filter",
                "status": "pass",
                "comments": f"Currency filter is working. Price changed from {initial_price} to {updated_price}"
            }
        else:
            return {
                "page_url": page_url,
                "testcase": "Currency filter",
                "status": "fail",
                "comments": f"Currency did not change. Price remains {initial_price}"
            }

    except TimeoutException as e:
        return {
            "page_url": page_url,
            "testcase": "Currency filter",
            "status": "fail",
            "comments": f"Timeout waiting for element: {str(e)}"
        }

    except NoSuchElementException as e:
        return {
            "page_url": page_url,
            "testcase": "Currency filter",
            "status": "fail",
            "comments": f"Element not found: {str(e)}"
        }

    except Exception as e:
        return {
            "page_url": page_url,
            "testcase": "Currency filter",
            "status": "fail",
            "comments": f"Error occurred: {str(e)}"
        }
