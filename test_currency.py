from selenium.webdriver.support.ui import WebDriverWait as wev
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time

def test_currency_filter(driver, page_url):
    results = []
    driver.get(page_url)

    try:
        # Wait for the price elements to load
        wev(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "js-price-value"))
        )

        # Attempt to locate the currency dropdown menu
        try:
            currency_menu = wev(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "js-currency-sort-footer"))
            )
        except TimeoutException:
            currency_menu = driver.find_element(By.CSS_SELECTOR, "#js-currency-sort-footer")

        # Scroll to the dropdown and ensure it's in view
        driver.execute_script("arguments[0].scrollIntoView(true);", currency_menu)
        time.sleep(5)

        # Click the dropdown using JavaScript or fallback to ActionChains
        try:
            driver.execute_script("arguments[0].click();", currency_menu)
        except Exception:
            ActionChains(driver).move_to_element(currency_menu).click().perform()

        time.sleep(5)

        # Collect all available currency options
        currency_list = driver.find_elements(By.CSS_SELECTOR, "#js-currency-sort-footer .select-ul li")
        print(f"Total currency options found: {len(currency_list)}")

        for option in currency_list:
            try:
                # Retrieve the currency code and symbol
                currency_code = option.get_attribute("data-currency-country") or "Unknown"
                currency_symbol = option.find_element(By.TAG_NAME, "p").text.strip()

                # Select the currency option
                driver.execute_script("arguments[0].click();", option)

                # Wait until the price values reflect the selected currency
                wev(driver, 10).until(
                    EC.text_to_be_present_in_element((By.CLASS_NAME, "js-price-value"), currency_symbol)
                )

                # Gather the updated price values
                price_elements = driver.find_elements(By.CLASS_NAME, "js-price-value")
                updated_prices = [element.text for element in price_elements]

                # Verify all prices display the correct currency symbol
                test_success = all(currency_symbol in price for price in updated_prices)

                results.append({
                    "page_url": page_url,
                    "testcase": f"Currency Change to {currency_code}",
                    "status": "pass" if test_success else "fail",
                    "comments": f"Prices displayed: {updated_prices}"
                })

                # Reopen the currency dropdown for the next iteration
                driver.execute_script("arguments[0].click();", currency_menu)
                time.sleep(5)

            except Exception as error:
                results.append({
                    "page_url": page_url,
                    "testcase": f"Currency Test for {currency_code}",
                    "status": "fail",
                    "comments": f"Error encountered: {str(error)}"
                })

    except Exception as critical_error:
        print(f"An error occurred during the currency test: {str(critical_error)}")
        results.append({
            "page_url": page_url,
            "testcase": "Currency Test",
            "status": "fail",
            "comments": f"Critical error: {str(critical_error)}"
        })

    return results
