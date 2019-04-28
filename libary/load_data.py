# coding=utf-8
# author:  henry chang
# email : henrychang1413@gmail.com


import os
import xlrd
import xlwt

excelfile = os.path.dirname(os.path.abspath('.')) + "\\data\\test_data.xlsx"

class LoadTestData:
    def __init__(self, testfile):
        self.testfile = testfile

    def load_data(self):
        # open excel file
        excel = xlrd.open_workbook(self.testfile)

        # get sheet table
        table = excel.sheet_by_name('Sheet1')

        #get rows
        nrows = table.nrows
        test_data = []
        for i in range(1, nrows):
            test_data.append(table.row_values(i))

        # return test_data
        return test_data


# if __name__ == "__main__":

#     testdata = LoadTestData(excelfile)
#     data = testdata.load_data()
#     print(data)

