from django.test import TestCase

# Create your tests here.
class NewRequestTest(TestCase):
    '''
    Test new requests
    '''

    def test_home_page_returns_correct_html(self):
        '''
        test home page returns html
        '''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'registration/home.html')

    def test_register_page_returns_correct_html(self):
        '''
        test register page returns correct html
        '''
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')
