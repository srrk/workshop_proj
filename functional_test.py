from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_user_can_register(self):
        '''
        tests whether user can visit the site and register
        '''
        # Shruthi comes to know about new workshop program
        # She is eager to know more details.
        # She visits the URL received in email.
        self.browser.get('http://localhost:8000')

        # She sees the title of web page as BRAF Summer Camp
        self.assertIn(self.browser.title, 'BRAF Summer Workshop')

        # Shruti got interested after reading the prospects of workshop
        # Like handson training, certification and a surprise gift.
        items = self.browser.find_elements_by_tag_name('li')
        key_words = ['handson', 'certification', 'gift']
        for key_word in key_words:
            self.assertIn(key_word, [item.text for item in items])

        # Then she clicks to register for the workshop.
        self.browser.find_element_by_id('register').click()

        # She notices a new form requesting her name, email.
        # She enters her name and email, and submits.
        register_form = self.browser.find_element_by_id\
                ('register-form')
        register_form.find_element_by_name('username').\
                sendkeys('shruti')
        register_form.find_element_by_name('email').\
                sendkeys('rajeshs@cdac.in')
        register_form.find_element_by_name('submit').\
                click()

        # She gets a confirmation page, saying her registration is
        # confirm and she will get a email to that effect.
        self.assertIn('confirmed', self.browser.find_element_by_tag_name('body').text)

        # Shruti smiles and thinks she should tell others also
        # for registration.

        ## Remainder.
        self.fail('Complete Test')

    #def test_admin_can_view_registered_users(self):

        # Admin(rajesh) receives an email saying that a user(shruti) registered
        # for email

        # Admin(rajesh) is happy that users are showing interested and he
        # wants who are the registered users.

        # He visits the admin page and logins.

        # He clicks the link of registered users.

        # He observers the list containing recent registered user on top.

        # He also observes that a playful registration like spam entries also
        # registered.

        # He selects those spam entries and clicks 'deregister' button on top
        # pass

if __name__ == '__main__':
    unittest.main(warnings='ignore')
