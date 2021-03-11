from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElementList():
    def findElementList(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"

        driver = webdriver.Chrome()
        driver.get(baseURL)

        elements = driver.find_elements(By.CLASS_NAME, "inputs")

        # elements = driver.find_elements_by_class_name("inputs")

        if elements is not None:
            print(len(elements))



object1 = FindElementList()
object1.findElementList()