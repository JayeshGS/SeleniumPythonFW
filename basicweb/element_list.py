from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ElementInteraction:

    def action_on_element(self):

        try:
            baseurl = "https://letskodeit.teachable.com/p/practice"
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.get(baseurl)
            driver.implicitly_wait(10)

            elements = driver.find_elements(By.XPATH, "//*[contains(@name,'cars') and contains(@type,'radio')]")
            size = len(elements)
            assert size == 3
            print("number of element = " + str(size))
            print(elements[:])

            for radiobutton in elements:
                isSelect = radiobutton.is_selected()

                if not isSelect:
                    radiobutton.click()
                    time.sleep(2)


        finally:
            driver.quit()


test = ElementInteraction()
test.action_on_element()