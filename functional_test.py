from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_user_can_register(self):
        '''
        tests whether user can visit 
        the site and register
        '''
        # Shruthi comes to know about new workshop program
        # She is eager to know more details.
        # She visits the URL received in email.
        self.browser.get('http://localhost:8000')

        # She sees the title of web page as BRAF Summer Camp
        self.assertIn(self.browser.title, 'BRAF Summer Camp')

        ## Remainder.
        self.fail('Complete Test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
