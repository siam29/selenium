# save_results_to_excel.py

import pandas as pd

# Function to save results to Excel
def save_results(results, filename="test_results.xlsx"):
    df = pd.DataFrame(results)
    df.to_excel(filename, index=False, engine='openpyxl')
