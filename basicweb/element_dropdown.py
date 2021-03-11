from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class Elementdropdown:

    def action_on_dropdown(self):

        try:
            baseurl = "https://letskodeit.teachable.com/p/practice"
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.get(baseurl)
            driver.implicitly_wait(10)

            element = driver.find_element(By.XPATH, "//*[contains(@id,'carselect')]")
            sel = Select(element)

            sel.select_by_value("bmw")
            time.sleep(3)

            sel.select_by_index(1)
            time.sleep(3)

        finally:
            driver.quit()


test = Elementdropdown()
test.action_on_dropdown()
