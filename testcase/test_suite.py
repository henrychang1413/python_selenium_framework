
import time
import os
import unittest
from test_login_ormuco import TestOrmucoLogin
from HTMLTestRunner import HTMLTestRunner

def create_suite():
    testunit = unittest.TestSuite()
    testunit.addTest(TestOrmucoLogin("test1_login_username_invalid"))
    testunit.addTest(TestOrmucoLogin("test2_login_username_invalid2"))
    testunit.addTest(TestOrmucoLogin("test3_login_password_invalid"))
    testunit.addTest(TestOrmucoLogin("test4_login_password_invalid2"))
    testunit.addTest(TestOrmucoLogin("test5_login_ormuco_username_password_valid"))
    return testunit


if __name__ == '__main__':

    suite = create_suite()
    runner=unittest.TextTestRunner()

    ctime = time.strftime('%Y-%m-%d-%H_%M', time.localtime())
    rfile = 'login_report_' + ctime + '.html'
    report_file =  os.path.dirname(os.path.abspath('.')) + "\\report\\" + rfile
    fp = open(report_file, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title='Test login to ormuco ',
        description='test login ormuco with different username and password')

    runner.run(suite)
    fp.close()


