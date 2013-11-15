#/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = self.browser.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Jay heard about a cool new to-do list app online
        #so he goes to check it out
        self.browser.get('http://localhost:8000')

        #he notices the page title and header mention to-do lists

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        #he can enter a to-do item right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        #he types "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        #when he hits enter, the page updates and now shows
        # "1: Buy peacock feathers" as a to-do list item
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers',[row.text for row in rows])

        #there is still a text box to add another item
        #he enters "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        #the page updates again and now shows both items in to-do list
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        #he wonders if the site will remember his list and notices
        #that the site has generated a unique url for him 


        #he visits that url and the items are still there


        #satisfied mvp
        self.fail('Finish The Test!!!')
if __name__=='__main__':
    unittest.main(warnings='ignore')
