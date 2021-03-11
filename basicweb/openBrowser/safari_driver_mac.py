from selenium import webdriver
import time


class SafariDriverTest():
    def testMethod(self):
        driver = webdriver.Safari()
        driver.get("http://www.letskodeit.com")
        # time.sleep(10000)


# Create object
safariobject = SafariDriverTest()

# Instance of Method
safariobject.testMethod()
