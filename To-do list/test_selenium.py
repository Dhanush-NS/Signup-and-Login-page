from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (adjust the path to where you have your WebDriver)
driver = webdriver.Chrome('C:\chromedriver-win64')  # Update this path

try:
    # Open the website
    driver.get("http://127.0.0.1:8000/login/")  # Change to the URL of your Django app

    # Wait for the page to load
    time.sleep(2)

    # Locate the input elements by their name attributes
    name_input = driver.find_element_by_name("name")
    phone_input = driver.find_element_by_name("phone")
    email_input = driver.find_element_by_name("email")

    # Enter data into the input elements
    name_input.send_keys("testname")
    phone_input.send_keys("1234567890")
    email_input.send_keys("test@example.com")

    # Submit the form
    phone_input.send_keys(Keys.RETURN)

    # Wait for the response
    time.sleep(2)

    # Check if the login was successful (you'll need to adapt this to your own success criteria)
    assert "Welcome" in driver.page_source

    print("Test passed successfully!")
finally:
    # Close the browser
    driver.quit()
