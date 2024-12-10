# main.py

from setup_driver import setup_driver
from test_html_tag_sequence import test_html
from save_results_to_excel import save_results
from h1_tag import test_h1_tag_existence
from image import test_image
from save_result import save_results_to_multiple_sheets
from Scraped_Data import scrape_data
from url import test_url
from test_currency import test_currency_filter
def main():
    page_url = "https://www.alojamiento.io/"
    driver = setup_driver()

    # Collect test results
    test_results = []
    test_results.extend(test_html(driver, page_url))
    print('Test HTML...')
    test_results.extend(test_h1_tag_existence(driver, page_url))
    print('Test H1 tag...')
    test_results.extend(test_image(driver, page_url))
    print('Test Image...')
    test_results.extend(test_url(driver,page_url))
    print('Test url...')
    test_results.extend(test_currency_filter(driver,page_url))
    print('Test Currency...')


    # Collect scraped data
    scraped_data = scrape_data(driver, page_url)
    print('Scraped data...')

    # Save results to Excel with multiple sheets
    save_results_to_multiple_sheets(test_results, scraped_data)

    # Close the browser
    driver.quit()
    print("Test results saved to test_results1.xlsx")

if __name__ == "__main__":
    main()
