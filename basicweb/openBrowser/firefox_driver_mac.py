from selenium import webdriver


class RunFireFoxBrowserTest():
    def testMethod(self):
        # driver = webdriver.Firefox(executable_path="/Users/jayesh/Documents/Trainings/Selenium_Py_Framework/drivers/geckodriver")
        driver = webdriver.Firefox()
        driver.get("http://www.letskodeit.com")
        driver.implicitly_wait(10000)
        driver.quit()


firefox1 = RunFireFoxBrowserTest()
firefox1.testMethod()
