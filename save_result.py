# save_result.py

import pandas as pd

def save_results_to_multiple_sheets(results, scraped_data, filename="test_results1.xlsx"):
    with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
        # Save test results to the first sheet
        results_df = pd.DataFrame(results)
        results_df.to_excel(writer, sheet_name="Test Results", index=False)

        # Save scraped data to the second sheet
        if not scraped_data.empty:
            scraped_data.to_excel(writer, sheet_name="Scraped Data", index=False)
