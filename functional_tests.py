#/usr/bin/env python

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Jay heard about a cool new to-do list app online
        #so he goes to check it out
        self.browser.get('http://localhost:8000')

        #he notices the page title and header mention to-do lists
        self.assertIn('To-Do', self. browser.title)
        self.fail('Finish The Test!!!')
        #he can enter a to-do item right away

        #he types "Buy peacock feathers" into a text box


        #when he hits enter, the page updates and now shows
        # "1: Buy peacock feathers" as a to-do list item


        #there is still a text box to add another item
        #he enters "Buy peacock feathers to make a fly"


        #the page updates again and now shows both items in to-do list


        #he wonders if the site will remember his list and notices
        #that the site has generated a unique url for him 


        #he visits that url and the items are still there


        #satisfied mvp

if __name__=='__main__':
    unittest.main(warnings='ignore')
