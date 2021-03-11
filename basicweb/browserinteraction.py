from selenium import webdriver
import time


class BrowserInteraction:
    def actions(self):

        try:
            driver = webdriver.Firefox()
            baseurl = "https://letskodeit.com/courses/"

            # Get URl
            driver.get(baseurl)

            # Get Header
            title = driver.title
            print("title of page = " + str(title))

            # Get Current URl
            current_url = driver.current_url
            print("current url = " + str(current_url))

            # Browser Refresh
            driver.refresh()
            print("browser refresh")

            # Get page source
            pagesource = driver.page_source
            file = open("pagesource.txt", "w+")
            file.write(pagesource)
            file.close()
            print("pagesource.txt file update")

            # Get on step Back
            driver.back()
            time.sleep(2)
            back_url = driver.current_url
            print("url after back = " + back_url)


        finally:
            driver.quit()


act = BrowserInteraction()
act.actions()
