# Automation_framework introduction

python automation framework design for UI test and interface test.  this framework use Python3 unittest framework. include 3 suites.

a: test login  "uat.ormuco.com" with different username and password

b: test google search with different keywords.

c: test number convert functions, such as binary convert decimal, decimal convert to Hexadimal

# How to run the framework?

1). Install all the dependencies
    pip install -r requirements.txt

2). Testcases are located inside testcase
    my_framework/testcase

3). execute python unittest command to run test suites.
    it will generate HTML report under report folder

    python -m unittest test_suite


# Test report 

![alt text](https://github.com/henrychang1413/python_selenium_framework/blob/master/report.png)

