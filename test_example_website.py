from selenium import webdriver
from selenium.webdriver.common.by import By

# Test Case 1: Verify Page Title
def test_verify_page_title():
    driver = webdriver.Chrome()
    driver.get('http://www.example.com')
    page_title = driver.title
    expected_title = 'Example Domain'
    assert page_title == expected_title, f'Expected title: {expected_title}, Actual title: {page_title}'
    driver.quit()

# Test Case 2: Check Page Header
# https://www.selenium.dev/documentation/webdriver/elements/finders/
def test_check_page_header():
    driver = webdriver.Chrome()
    driver.get('http://www.example.com')
    header_element = driver.find_element(By.TAG_NAME, 'h1')     # import By needed
    expected_text = 'Example Domain'
    assert expected_text in header_element.text, f'Expected text: {expected_text}, Actual text: {header_element.text}'
    driver.quit()


# Test Case 3: Click a Link
# https://www.selenium.dev/documentation/webdriver/elements/locators/
def test_click_link():
    driver = webdriver.Chrome()
    driver.get('http://www.example.com')
    link_element = driver.find_element(By.LINK_TEXT,'More information...')
    link_element.click()
    new_page_title = driver.title
    assert new_page_title != 'Example Domain', 'Page title didn\'t change after clicking the link.'
    driver.quit()


# Test Case 4: Submit a Form
def test_submit_form():
    driver = webdriver.Chrome()
    driver.get('https://duckduckgo.com')
    search_input = driver.find_element(By.NAME, 'q')
    search_input.send_keys('Test query')

    # In the Safari Web Inspector, right clicking an element allows you to copy the XPath
    submit_button = driver.find_element(By.XPATH, '//*[@id="searchbox_homepage"]/div/div/button')
    submit_button.click()

    # Get result elements
    search_results = driver.find_elements(By.TAG_NAME, 'h2')
    assert len(search_results) > 0, f'No results found for "{search_input}"'
    driver.quit()
