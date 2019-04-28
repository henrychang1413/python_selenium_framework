# coding=utf-8
# author:  henry chang
# email : henrychang1413@gmail.com

import time
import os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from logger import Logger

# create a logger instance
logger = Logger(logger="OperatePage").getlog()

class OperatePage(object):
    """ define one page base class other page will inherit this page operations """

    def __init__(self, driver=None):
        self.driver = driver

    # quit browser and end testing
    def page_quit(self):
        self.driver.quit()

    # forword browser
    def page_forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    # back browser
    def page_back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    # waitting
    def page_wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    # refresh
    def page_refresh(self):
        self.driver.refresh()
        logger.info("Refresh page .")
        time.sleep(2)


    # close current window
    def page_close(self):
        try:
            self.driver.close()
            logger.info("Closing the browser.")
        except NameError as e:
            logger.error("Failed to close the browser with %s" % e)

    # save picture
    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '\\screenshots\\'
        ctime = time.strftime('%Y-%m-%d-%H_%M', time.localtime())
        screen_name = file_path + ctime + '.png'

        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Take screenshot and save to folder: %s " % (screen_name))
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    # locate element
    def find_element(self, selector):
        element = None
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        By = selector.split('=>')[0]
        value = selector.split('=>')[1]

        try:
            if By == 'id':
                element = self.driver.find_element_by_id(value)
            elif By == 'name':
                element = self.driver.find_element_by_name(value)
            elif By == 'class':
                element = self.driver.find_element_by_class_name(value)
            elif By == 'link':
                element = self.driver.find_element_by_link_text(value)
            elif By == 'plink':
                element = self.driver.find_element_by_partial_link_text(value)
            elif By == 'tag':
                element = self.driver.find_element_by_tag_name(value)
            elif By == 'xpath':
                element = self.driver.find_element_by_xpath(value)
            elif By == 'css':
                element = self.driver.find_element_by_css_selector(value)
            else:
                raise NameError("Please enter a valid type of elements.")
                logger.error(" not find element : %s " %selector)
            logger.info("Successe to find element by %s via value: %s " % ( By, value))

        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)
            self.get_windows_img()

        return element

    #for drop_box select element
    def select_child_element(self, selector):
        element = None
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        By = selector.split('=>')[0]
        val = selector.split('=>')[1]

        try:
            if By == "xpath":
                Select(self.driver.find_element_by_xpath(val))
            elif By == "id":
                Select(self.driver.find_element_by_id(val))
            elif By == "name":
                Select(self.driver.find_element_by_name(val))
            elif By == "link":
                Select(self.driver.find_element_by_link_text(val))
            elif By == "plink":
                Select(self.driver.find_element_by_partial_link_text(val))
            else:
                raise NameError("Please enter a valid type of elements.")
                logger.error(" not find element : %s " %selector)

            logger.info("Successe to find element by %s via value: %s " % ( By, value))

        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)
            self.get_windows_img()

        return element


    def get_selector_text(self,selector):
        ele = self.find_element(selector)
        return ele.text

    # simulate keyboard to input
    def selector_input(self, selector, text):
        ele = self.find_element(selector)
        ele.clear()
        try:
            ele.send_keys(text)
            logger.info("input \' %s \' " % text)
        except NameError as e:
            logger.error("Failed to input box with %s" % e)
            self.get_windows_img()

    # clear data from input box
    def selector_clear(self, selector):
        ele = self.find_element(selector)
        try:
            ele.clear()
            logger.info("Clear input box before typing.")
        except NameError as e:
            logger.error("Failed to clear input box with %s" % e)
            self.get_windows_img()

    # click element
    def selector_click(self, selector):
        ele = self.find_element(selector)
        try:
            ele.click()
            logger.info("The element \' %s \' was clicked." % ele.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    # get title from page
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    def switch_frame(self, loc):
        return self.driver.switch_to.frame(loc)

    def switch_alert(self):
        return self.driver.switch_to.alert()

    def switch_alert_close(self):
        self.driver.switch_to.alert().dismiss()

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)
