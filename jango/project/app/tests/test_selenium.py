from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest

class MySeleniumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Optional: Run Chrome in headless mode
        chrome_options.binary_location = 'C:\chromedriver-win64'  # Path to Chrome executable
        
        # Initialize WebDriver with Chrome options
        cls.selenium = webdriver.Chrome(options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        # Close the WebDriver instance after all tests are run
        cls.selenium.quit()

    def test_example(self):
        # Your test code here
        self.selenium.get("http://www.example.com")
        self.assertIn("Example Domain", self.selenium.title)

if __name__ == '__main__':
    unittest.main()
