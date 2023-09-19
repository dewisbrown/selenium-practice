from selenium import webdriver

# Test Case 1: Verify Page Title
def test_verify_page_title():
    driver = webdriver.Chrome()
    driver.get('http://www.example.com')
    page_title = driver.title
    expected_title = 'Example Domain'
    assert page_title == expected_title, f'Expected title: {expected_title}, Actual title: {page_title}'
    driver.quit()
