from selenium import webdriver


class BrowserInteractions():
    def test(self):
        driver = webdriver.Firefox()
        driver.delete_all_cookies()

        driver.maximize_window()
        print("Maximise browser successful")

        driver.get("https://letskodeit.teachable.com/p/practice")

        print("Title of Page = " + driver.title)

        print("Current URL = " + driver.current_url)
        
        # driver.refresh()
        # print("Refresh successful")
        
        driver.implicitly_wait(2)
        
        driver.find_element_by_css_selector('.btn-style.class1.class2').click()
        print("Page 2 URL = " + driver.current_url)

        driver.back()
        print("First page URL = " + driver.current_url)

        driver.forward()
        print("Page 2 URL again = " + driver.current_url)

        driver.quit()


object1 = BrowserInteractions()
object1.test()
