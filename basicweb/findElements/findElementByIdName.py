from selenium import webdriver
from selenium.webdriver.common.by import By

class FindElementByIdName():

    def findElementByIDName(self):
        
        baseURL = "https://letskodeit.teachable.com/p/practice"

        driver = webdriver.Chrome()
        driver.get(baseURL)
        
        elementByID = driver.find_element_by_id("bmwradio")
        if elementByID is not None:
            print("We found the element by ID")
            
        elementByName = driver.find_element_by_name("cars")
        if elementByName is not None:
            print("We found the element by Name")


# create a object
object1 = FindElementByIdName()

object1.findElementByIDName()