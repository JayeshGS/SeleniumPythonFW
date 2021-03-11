from selenium import webdriver


class FindElementByCSSID():
    def findByCSSID(self):

        baseURL = "https://letskodeit.teachable.com/p/practice"

        driver = webdriver.Chrome()
        driver.get(baseURL)

        element1 = driver.find_element_by_css_selector("button[class = 'btn-style class1']")

        if element1 is not None:
            print(element1.text)
        else:
            print("Error")

        element2 = driver.find_element_by_css_selector(".btn-style.class1.class2")

        if element1 is not None:
            print(element2.text)
        else:
            print("Error")

        element3 = driver.find_element_by_css_selector("input.inputs")

        if element1 is not None:
            print(element3.get_attribute('placeholder'))
        else:
            print("Error")


object1 = FindElementByCSSID()
object1.findByCSSID()
