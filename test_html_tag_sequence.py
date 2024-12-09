# test_html_tag_sequence.py

from selenium.webdriver.common.by import By

# HTML Tag Sequence Test
def test_html(driver, page_url):
    html_list=[]
    driver.get(page_url)
    tags = ["h1", "h2", "h3", "h4", "h5", "h6"]
    for i, tag in enumerate(tags):
        try:
            driver.find_element(By.TAG_NAME, tag)
        except:
            html_list.append({"page_url": page_url, "testcase": "HTML tag sequence", "status": "fail", "comments": f"Missing {tag} tag at position {i+1}"})
    html_list.append({"page_url": page_url, "testcase": "HTML tag sequence", "status": "pass", "comments": "All tags h1-h6 are present"})

    return html_list
