# -*- coding:utf-8 -*-
# author:  henry chang
# email : henrychang1413@gmail.com

import os
import time
import globalparam
from selenium import webdriver
from logger import Logger

logger = Logger(logger="BrowserEngine").getlog()

class BrowserEngine(object):

    def __init__(self, driver=None, browser="Chrome"):
        self.driver = driver
        self.browser = browser

    # read the browser type from config.ini file, return the driver
    def open_browser(self):

        if self.browser == "Firefox":
            self.driver = webdriver.Firefox()
            logger.info("Open firefox browser.")
        elif self.browser == "Chrome":
            chrome_driver_path = globalparam.readcf.getVal("webdriver", "chromedriver")
            self.driver = webdriver.Chrome(chrome_driver_path)
            logger.info("Open Chrome browser.")
        elif self.browser == "IE":
            ie_driver_path = globalparam.readcf.getVal("webdriver", "iedriver")
            self.driver = webdriver.Ie(ie_driver_path)
            logger.info("Open IE browser.")
        else:
            raise NameError("Please enter a valid browser.")

        self.driver.maximize_window()
        return self.driver

    # quit browser and end testing
    def open_url(self, url=None):
        if url == None:
            url = globalparam.readcf.getVal("testServer", "URL")

        self.driver.get(url)
        logger.info("Open url: %s" % url)

    def quit_browser(self):
        logger.info("Quit the browser.")
        self.driver.quit()


# if __name__ == "__main__":

#     A= BrowserEngine()
#     A.open_browser()
#     A.open_url()
#     A.quit_browser()

