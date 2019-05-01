# coding=utf-8
# author:  henry chang
# email : henrychang1413@gmail.com

import unittest
from libary.number_convert import *
from libary.logger import Logger

logger = Logger(logger="TestNumConvert").getlog()

class TestNumConvert(unittest.TestCase):

    @classmethod
    def setUp(cls):
        """ setup """
        logger.info('\n========== setup ==========')
        pass

    @classmethod
    def tearDown(cls):
        """ cleanup """
        logger.info('\n========== teardown ==========')
        pass

    def test1_binary_convert_decimal(self):
        logger.info('\n=== test case: test_binary_convert_decimal ===\n')
        input_data_list = ['1101', '1111', '011', '11110001']
        for ele in input_data_list:
            BiToDec = BinarytoDecimal(ele)
            dec = (BiToDec.covertx())
            logger.info('binary ==> decimal : %s => %s'%(ele,dec))

    def test2_decimal_convert_binary(self):
        logger.info('\n=== test case: test_decimal_convert_binary ===\n')
        input_data_list = [13, 15, 3, 241]
        for ele in input_data_list:
            DecToBi = DecimalToBinary(ele)
            bina = (DecToBi.covertx())
            logger.info('decimal ==> binary : %s => %s'%(ele,bina))

    def test3_Hexadecimal_convert_decimal(self):
        logger.info('\n=== test case: test_Hexadecimal_convert_decimal ===\n')
        input_data_list = ['1DB', '235', 'FD23A', '992']
        for ele in input_data_list:
            DecToBi = HexadecimalToDecimal(ele)
            dec = (DecToBi.covertx())
            logger.info('Hexadecimal ==> decimal : %s => %s'%(ele,dec))


    def test4_decimal_convert_Hexadecimal(self):
        logger.info('\n=== test case: test_decimal_convert_Hexadecimal ===\n')
        input_data_list = [475, 565, 1036858, 2450]
        for ele in input_data_list:
            DecToBi = HexadecimalToDecimal(ele)
            dec = (DecToBi.covertx())
            logger.info('decimal ==> Hexadecimal : %s => %s'%(ele,dec))


# if __name__ == "__main__":
#     unittest.main()
#     #unittest.main(verbosity=2)

