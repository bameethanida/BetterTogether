from django.test import LiveServerTestCase
from selenium import webdriver


class SeleniumTestCase(LiveServerTestCase):
    username = 'bamee'
    password = '1212312121'

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=options)
        super(SeleniumTestCase, self).setUp()

    def tearDown(self):
        self.browser.quit()
        super(SeleniumTestCase, self).tearDown()

    def test_click_login(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_class_name('google-button').click()
        expected_url = self.live_server_url + '/accounts/google/login/'
        self.assertEqual(self.browser.current_url, expected_url)
