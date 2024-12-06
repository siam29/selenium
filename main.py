# main.py
from setup_driver import setup_driver
from test_html_tag_sequence import test_html
from save_results_to_excel import save_results
from h1_tag import test_h1_tag_existence
from image import test_image



# Main function to run the tests
def main():
    page_url = "https://www.alojamiento.io/"
    driver = setup_driver()
    
    # Run the test case
    test_results = []
    test_results.append(test_html(driver, page_url))
    test_results.append(test_h1_tag_existence(driver, page_url))
    test_results.append(test_image(driver,page_url))

    
    # Save results to Excel
    save_results(test_results)

    # Close the browser
    driver.quit()
    print("Test results saved to test_results.xlsx")

if __name__ == "__main__":
    main()
