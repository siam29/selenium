import pandas as pd

def save_results_to_multiple_sheets(results, scraped_data, filename="test_results.xlsx"):
    with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
        # Save test results to the first sheet
        results_df = pd.DataFrame(results)
        results_df.to_excel(writer, sheet_name="Test Results", index=False)

        # Save scraped data to the second sheet
        scraped_df = pd.DataFrame(scraped_data)
        scraped_df.to_excel(writer, sheet_name="Scraped Data", index=False)

# Example usage
results = [{'Test': 'HTML Test', 'Status': 'Pass'}, {'Test': 'H1 Tag Test', 'Status': 'Fail'}]
scraped_data = {'SiteURL': ['https://example.com'], 'SiteName': ['Example Site']}

save_results_to_multiple_sheets(results, scraped_data)
