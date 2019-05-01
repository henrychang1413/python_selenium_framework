# -*- coding:utf-8 -*-
# author:  henry chang
# email : henrychang1413@gmail.com
# date  : 2019-4-29

import time
import os
import unittest
from libary.globalparam import *
from HTMLTestRunner import HTMLTestRunner
from test_suite_number_convert import *
from test_suite_google_search  import *
from test_suite_ormuco_login   import *

#####
suite_number_convert = NumConvertSuite()
suite_google_search  = GoogleSearchSuite()
suite_ormuco_login   = OrmuSuite()

TotalSuite=unittest.TestSuite((suite_number_convert,
                          suite_google_search,
                          suite_ormuco_login,
        ))


#TotalSuite=unittest.TestSuite((suite_number_convert))
#define report path and format
ctime = time.strftime('%Y-%m-%d-%H_%M', time.localtime())
rfile = 'login_report_' + ctime + '.html'
report_file = os.path.join(report_path, rfile)

fp = open(report_file, 'wb')
runner = HTMLTestRunner(
    stream=fp,
    title='Run all cases',
    description='include 3 suites, test different modules')

runner.run(TotalSuite)
fp.close()


