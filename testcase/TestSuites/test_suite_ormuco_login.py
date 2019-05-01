# -*- coding:utf-8 -*-
# author:  henry chang
# email : henrychang1413@gmail.com
# date  : 2019-4-29

import unittest
from TestOrmucoLogin.test_login_ormuco import TestOrmucoLogin

def OrmuSuite():
    testunit = unittest.TestSuite()
    testunit.addTest(TestOrmucoLogin("test1_login_username_invalid"))
    testunit.addTest(TestOrmucoLogin("test2_login_username_invalid2"))
    testunit.addTest(TestOrmucoLogin("test3_login_password_invalid"))
    testunit.addTest(TestOrmucoLogin("test4_login_password_invalid2"))
    testunit.addTest(TestOrmucoLogin("test5_login_ormuco_username_password_valid"))

    return testunit

