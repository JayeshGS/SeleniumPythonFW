from selenium import webdriver


class SeleniumSafari:

    def seleniumsafaritest(self):
        driver = webdriver.Safari()
        driver.get("http://www.letskodeit.com")


ff = SeleniumSafari()
ff.seleniumsafaritest()

