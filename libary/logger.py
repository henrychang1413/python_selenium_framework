# _*_ coding: utf-8 _*_
# author:  henry chang
# email : henrychang1413@gmail.com

import logging
import time
import os.path
import globalparam

class Logger(object):

    def __init__(self, logger):
        ''' log path , log level , save log to direct file '''

        # create one logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # create one handler to write log into one file
        ctime = time.strftime('%Y-%m-%d-%H_%M', time.localtime())
        lname =  ctime + '.log'
        log_name = os.path.join(globalparam.log_path, lname)

        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        #create another handle to output control platform
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        #define handle ouput format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # add handler  for logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger



