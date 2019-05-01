# -*- coding:utf-8 -*-
# author:  henry chang
# email : henrychang1413@gmail.com
# date  : 2019-4-29

import unittest
from TestNumberConvert.test_number_convert import TestNumConvert

def NumConvertSuite():
    testunit = unittest.TestSuite()
    testunit.addTest(TestNumConvert("test1_binary_convert_decimal"))
    testunit.addTest(TestNumConvert("test2_decimal_convert_binary"))
    testunit.addTest(TestNumConvert("test3_Hexadecimal_convert_decimal"))
    testunit.addTest(TestNumConvert("test4_decimal_convert_Hexadecimal"))

    return testunit


