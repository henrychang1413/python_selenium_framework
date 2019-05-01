# -*- coding:utf-8 -*-
# author:  henry chang
# email : henrychang1413@gmail.com
# date  : 2019-4-29

import unittest
from TestGoogleSearch.test_google_search import TestGoogleSearch

def GoogleSearchSuite():
    testunit = unittest.TestSuite()
    testunit.addTest(TestGoogleSearch("test1_search_gggg"))
    testunit.addTest(TestGoogleSearch("test1_search_python"))

    return testunit




