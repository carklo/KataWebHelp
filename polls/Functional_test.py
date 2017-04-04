from unittest import TestCase
from selenium import webdriver

class FunctionalTest (TestCase):


    def setUp(self):
        self.browser= webdriver.Firefox(executable_path=r'../geckodriver.exe')
        self.browser.get('http://inventwithpython.com')

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)