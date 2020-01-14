from selenium import webdriver
import unittest

class MainTest(unittest.TestCase):

	def setUp(self):
    # This method is called always on beginning of test. It starts web browser. 
		self.browser = webdriver.Firefox(
            executable_path="./geckodriver")

	def tearDown(self):
    # This metods is called always on the end of test (even when failed). It closes web browser.
		self.browser.quit()

	def test_open_main(self):
    # First simple test of desktop append 
		self.browser.get('http://localhost:8000')
        # load default web page (on port 8000)
        
		self.assertIn('AiSD', self.browser.title)
		# Find word 'Desktop' in webpage title
        
		self.fail('All tests passed!')
        # Finish test

if __name__ == '__main__':
	unittest.main()