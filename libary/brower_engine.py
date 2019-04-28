# -*- coding:utf-8 -*-
# author:  henry chang
# email : henrychang1413@gmail.com

import os
from  configparser import ConfigParser
from selenium import webdriver
from logger import Logger

logger = Logger(logger="BrowserEngine").getlog()

class BrowserEngine(object):
    configfile= os.path.dirname(os.path.abspath('.')) + "\\config\\config.ini"
    def __init__(self, driver=None):
        self.driver = driver

    # read the browser type from config.ini file, return the driver
    def open_browser(self):
        config = ConfigParser()
        config.read(BrowserEngine.configfile)

        browser = config.get("browserType", "browserName")
        logger.info("select %s browser." % browser)
        url = config.get("testServer", "URL")
        logger.info("The test url is: %s" % url)

        if browser == "Firefox":
            self.driver = webdriver.Firefox()
            logger.info("Open firefox browser.")
        elif browser == "Chrome":
            chrome_driver_path = config.get("webdriver", "chromedriver")
            self.driver = webdriver.Chrome(chrome_driver_path)
            logger.info("Open Chrome browser.")
        elif browser == "IE":
            ie_driver_path = config.get("webdriver", "iedriver")
            self.driver = webdriver.Ie(ie_driver_path)
            logger.info("Open IE browser.")

        self.driver.get(url)
        logger.info("Open url: %s" % url)
        self.driver.maximize_window()
        logger.info("Maximize the current window.")
        self.driver.implicitly_wait(20)
        logger.info("Set implicitly wait 20 seconds.")
        return self.driver

    def quit_browser(self):
        logger.info("Quit the browser.")
        self.driver.quit()


# if __name__ == "__main__":

#     A= BrowserEngine()
#     A.open_browser()
#     A.quit_browser()

