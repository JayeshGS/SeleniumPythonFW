from selenium import webdriver


class ChromeBrowserTest():
    def testMethod(self):
        # driver = webdriver.Chrome(executable_path="/Users/jayesh/Documents/Trainings/Selenium_Py_Framework/drivers/chromedriver 4")
        driver = webdriver.Chrome()
        driver.get("http://www.letskodeit.com")


chromeTest = ChromeBrowserTest()
chromeTest.testMethod()
