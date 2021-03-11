from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ElementInteraction:

    def action_on_element(self):

        try:
            baseurl = "https://letskodeit.com/"
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.get(baseurl)
            driver.implicitly_wait(10)

            # click on login
            loginlink = driver.find_element_by_xpath("//div[contains(text(),'Sign Up or Log In')]")
            loginlink.click()

            loginpageurl = driver.current_url
            print("login page url = " + loginpageurl)

            email_box = driver.find_element(By.CSS_SELECTOR, "#email")
            print("email field is displayed = " + str(email_box.is_displayed()))
            print("email field is enabled = " + str(email_box.is_enabled()))
            email_box.send_keys("test")

            password_box = driver.find_element(By.CSS_SELECTOR, "#password")
            password_box.send_keys("test")

            email_box.clear()
            email_box.send_keys("test123213")

        finally:
            driver.quit()


test = ElementInteraction()
test.action_on_element()
