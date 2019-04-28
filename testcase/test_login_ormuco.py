# coding=utf-8
# author:  henry chang
# email : henrychang1413@gmail.com


import time
import unittest
import os
from HTMLTestRunner import HTMLTestRunner
from libary.brower_engine import BrowserEngine
from libary.brower_operate import OperatePage
from libary.logger import Logger

logger = Logger(logger="TestOrmucoLogin").getlog()

class TestOrmucoLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ setup """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser()

    @classmethod
    def tearDownClass(cls):
        """ cleanup """
        cls.driver.quit()


    def test1_login_username_invalid(self):

        homepage = OperatePage(self.driver)
        homepage.page_refresh()

        username_box = "id=>username"
        username = 'henrychang'
        homepage.selector_input(username_box, username)
        time.sleep(2)

        password_box = "id=>password"
        password = 'ormu1234567890'
        homepage.selector_input(password_box, password)

        logger.info('Username :%s  Password:%s'%(username,password))
        time.sleep(2)

        button = "xpath=>//button[contains(text(),'Sign in')]"
        homepage.find_element(button)
        homepage.selector_click(button)
        time.sleep(3)
        homepage.get_windows_img()

        #assert login fail message
        warning_box = "xpath=>//span[@class='warning']"
        warning_text= homepage.get_selector_text(warning_box)
        logger.info('warning mesage:%s' %  warning_text)
        self.assertIn("user or password is incorrect", warning_text, msg=" assert login")



    def test2_login_username_invalid2(self):

        homepage = OperatePage(self.driver)
        homepage.page_refresh()

        username_box = "id=>username"
        username = 'henrychangdfffffffffffffffffffsfsfsddsfsfsfffdddddddddddddddddddddddddddssssssfss@gmail.com'
        homepage.selector_input(username_box, username)
        time.sleep(2)

        password_box = "id=>password"
        password = 'ormu1234567890'
        homepage.selector_input(password_box, password)

        logger.info('Username :%s  Password:%s'%(username,password))
        time.sleep(2)

        button = "xpath=>//button[contains(text(),'Sign in')]"
        homepage.find_element(button)
        homepage.selector_click(button)
        time.sleep(3)
        homepage.get_windows_img()

        #assert login fail message
        warning_box = "xpath=>//span[@class='warning']"
        warning_text= homepage.get_selector_text(warning_box)
        logger.info('warning mesage:%s' %  warning_text)
        self.assertIn("user or password is incorrect", warning_text, msg=" assert login")


    def test3_login_password_invalid(self):

        homepage = OperatePage(self.driver)
        homepage.page_refresh()

        username_box = "id=>username"
        username = 'henrychang1413@gmail.com'
        homepage.selector_input(username_box, username)
        time.sleep(2)

        password_box = "id=>password"
        password = 'ormu12345e'
        homepage.selector_input(password_box, password)

        logger.info('Username :%s  Password:%s'%(username,password))
        time.sleep(2)

        button = "xpath=>//button[contains(text(),'Sign in')]"
        homepage.find_element(button)
        homepage.selector_click(button)
        time.sleep(3)
        homepage.get_windows_img()

        #assert login fail message
        warning_box = "xpath=>//span[@class='warning']"
        warning_text= homepage.get_selector_text(warning_box)
        logger.info('warning mesage:%s' %  warning_text)
        self.assertIn("user or password is incorrect", warning_text, msg=" assert login")

    def test4_login_password_invalid2(self):

        homepage = OperatePage(self.driver)
        homepage.page_refresh()

        username_box = "id=>username"
        username = 'henrychang1413@gmail.com'
        homepage.selector_input(username_box, username)
        time.sleep(2)

        password_box = "id=>password"
        password = 'ormu123!!!!.....&&&&&&2342______!!!!!#####sljslafldajflasjdlsjlsajlsfsdfsfffdsfsdfsdfsfsfsgrhh45e'
        homepage.selector_input(password_box, password)

        logger.info('Username :%s  Password:%s'%(username,password))
        time.sleep(2)

        button = "xpath=>//button[contains(text(),'Sign in')]"
        homepage.find_element(button)
        homepage.selector_click(button)
        time.sleep(3)
        homepage.get_windows_img()

        #assert login fail message
        warning_box = "xpath=>//span[@class='warning']"
        warning_text= homepage.get_selector_text(warning_box)
        logger.info('warning mesage:%s' %  warning_text)
        self.assertIn("user or password is incorrect", warning_text, msg=" assert login")

    def test5_login_ormuco_username_password_valid(self):
        homepage = OperatePage(self.driver)
        homepage.page_refresh()

        username_box = "id=>username"
        username = 'henrychang1413@gmail.com'
        homepage.selector_input(username_box, username)

        password_box = "id=>password"
        password = 'ormu1234567890'
        homepage.selector_input(password_box, password)

        logger.info('Username :%s  Password:%s'%(username,password))
        time.sleep(2)

        button = "xpath=>//button[contains(text(),'Sign in')]"
        homepage.find_element(button)
        homepage.selector_click(button)
        time.sleep(7)

        homepage.get_windows_img()
        print(homepage.get_page_title())
        page_title = homepage.get_page_title()
        logger.info(page_title)

        #verify login
        welcome_box = "xpath=>//*[@id='portal_main_scroll_content']/div/div[1]/h1"
        welcome_text= homepage.get_selector_text(welcome_box)
        logger.info('welcome mesage:%s' %  welcome_text)
        self.assertIn("Welcome to your Ormuco", welcome_text, msg=" assert login")


# if __name__ == "__main__":
#     unittest.main()


# if __name__ == '__main__':

#     testunit = unittest.TestSuite()
#     testunit.addTest(TestOrmucoLogin("test_login_username_invalid"))
#     testunit.addTest(TestOrmucoLogin("test_login_username_invalid2"))
#     testunit.addTest(TestOrmucoLogin("test_login_password_invalid"))
#     testunit.addTest(TestOrmucoLogin("test_login_password_invalid2"))
#     testunit.addTest(TestOrmucoLogin("test_login_ormuco_username_password_valid"))

#     ctime = time.strftime('%Y-%m-%d-%H_%M', time.localtime())
#     rfile = 'login_report_' + ctime + '.html'
#     report_file =  os.path.dirname(os.path.abspath('.')) + "\\report\\" + rfile
#     fp = open(report_file, 'wb')
#     runner = HTMLTestRunner(
#         stream=fp,
#         title='Test login to ormuco ',
#         description='test login ormuco with different username and password')

#     runner.run(testunit)

