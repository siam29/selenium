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

**Clone the Repository**
```
git clone https://github.com/siam29/selenium.git
```
**Navigate to the Project Directory**
```
cd selenium
```
**Create a Virtual Environment**
```
python3 -m venv myenv
```

**Activate the Virtual Environment**
- On Mac/Linux
```
source myenv/bin/activate
```
- On Windows
```
myenv\Scripts\activate
```
**Install Require Dependencies**
```
pip install -r requirements.txt
```
**Run the Project**
```
python main.py
```
## Output
```test_results1.xlsx``` – Contains test case results. It contain 2 sheet ```Test Results``` and ```Scraped Data```.
```Test Results``` look like this 
```
| page_url         | testcase                    | status | comments                         |
|------------------|-----------------------------|--------|----------------------------------|
| https://...      | Test HTML Elements          | pass   | All elements found               |
| https://...      | Currency Change to USD      | pass   | Updated prices: $100, $200       |
```
```Scraped Data``` – Contains scraped data:
```
| SiteURL          | CampaignID | SiteName      | Browser | CountryCode | IP           |
|------------------|------------|---------------|---------|-------------|--------------|
| https://...      | 12345      | Example Site  | Chrome  | US          | 192.168.0.1  |
```
## Connect with Me
If you have any questions, suggestions, or feedback, feel free to reach out to me through the following channels
- Email: almahmudsiam15@gmail.com
- GitHub: https://github.com/siam29
