# coding=utf-8
# author:  henry chang
# email : henrychang1413@gmail.com

import time
import unittest
import os
from libary.brower_engine import BrowserEngine
from libary.brower_operate import OperatePage
from libary.logger import Logger

logger = Logger(logger="TestGoogleSearch").getlog()
url = "https://www.google.ca"

class TestGoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ setup """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser()
        browse.open_url(url)

    @classmethod
    def tearDownClass(cls):
        """ cleanup """
        cls.driver.quit()

    def test1_search_gggg(self):
        logger.info('\n=== start to test case: test1_search_gggg ===\n')

        #open base page
        homepage = OperatePage(self.driver)
        homepage.page_refresh()

        page_tile = homepage.get_page_title()
        logger.info(page_tile)
        self.assertIn("Google", page_tile)

        search_box = "name=>q"
        input_txt = 'gggggg'
        homepage.selector_submit(search_box, input_txt)
        time.sleep(3)

        page_tile = homepage.get_page_title()
        logger.info(page_tile)
        self.assertIn("gggggg", page_tile)
        homepage.get_windows_img()


    def test1_search_python(self):
        logger.info('\n=== start to test case: test1_search_python ===\n')

        #open base page
        homepage = OperatePage(self.driver)
        homepage.page_refresh()

        page_tile = homepage.get_page_title()
        logger.info(page_tile)
        self.assertIn("Google", page_tile)

        search_box = "name=>q"
        input_txt = 'python'
        homepage.selector_submit(search_box, input_txt)
        time.sleep(2)

        page_tile = homepage.get_page_title()
        logger.info(page_tile)
        self.assertIn("python", page_tile)
        homepage.get_windows_img()


# if __name__ == "__main__":
#     unittest.main(verbosity=2)
