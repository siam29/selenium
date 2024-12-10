# Selenium Web Scraping and Testing Project
This project uses Selenium to perform web scraping and automated testing on a sample website. It includes functionalities like extracting data, verifying HTML elements, testing image availability, and currency filtering. The project outputs results to Excel files with multiple sheets for easy analysis.
## Description
This project automates the testing of a vacation rental details page on the website [alojamiento.io](https://www.alojamiento.io/) to validate essential elements and functionality. The script checks for various SEO-impacting test cases such as:
- **H1 Tag Existence**: Validates the presence of the H1 tag.
- **HTML Tag Sequence**: Ensures that the sequence of HTML tags (H1-H6) is correct.
- **Image Alt Attribute Validation**: Checks if the image elements have the alt attribute.
- **URL Status Code Test**: Verifies that all URLs on the page are functional (i.e., not 404).
- **Currency Filter**: Ensures that the property tiles' currency changes according to the selected filter.
- **Scrape Script Data**: Collects site information and records it in an Excel file.
## Requirements
- **Python 3.x**: Ensure Python is installed on your machine.
- **Libraries**: Use the following libraries for automation:
  - `Selenium`
  - `Pandas`
  - `webdriver-manager`
- **Web Browser**: Google Chrome or Firefox with the respective WebDriver.
- **Test Site**: [https://www.alojamiento.io/](https://www.alojamiento.io/)

## Setup this project
```
python3 -m venv myenv
```
```
source myenv/bin/activate
```
```
pip install -r requirements.txt
```
```
python main.py
```