#from selenium import webdriver
#
#browser = webdriver.Firefox()
#browser.get('http://localhost:8000')
#
#assert 'To-Do' in browser.title
#browser.quit()


from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                    inputbox.get_attribute('placeholder'),
                    'Enter a to-do item'
                )
        # She types "Buy peacock feathers" into a text box(Edith's hobby 
        # is trying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
                    any(row.text == '1: Buy peacock feathers' for row in rows)
                )
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
