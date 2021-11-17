from django.test import TestCase
from selenium import webdriver
import time
class TestViews(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.admin_url = 'http://localhost:8000/admin/'
        self.admin_logout_url = 'http://localhost:8000/admin/logout/'

    def testLoginOfAdminUser(self):
        self.driver.get(self.admin_url)
        self.driver.find_element_by_id('id_username').send_keys("admin")
        self.driver.find_element_by_id('id_password').send_keys("admin")
        self.driver.find_element_by_css_selector("input[type='submit']").click()
        self.driver.get(self.admin_logout_url)
        self.assertEquals(self.driver.current_url,self.admin_logout_url)
