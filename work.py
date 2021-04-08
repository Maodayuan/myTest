from selenium import webdriver
from time import sleep


class Work:

    def __init__(self, drivers):
        self.driver = drivers

    def login(self):
        self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('username').send_keys('maodayuan')
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys('Mdy4090@')
        self.driver.find_element_by_class_name('ant-btn').click()

    def click(self):
        self.driver.find_elements_by_class_name('ant-menu-item')[3].click()

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':

    url = ['http://new.nezha-test.compass.ym/']

    for i in url:
        print(i)
        driver = webdriver.Chrome()
        driver.get(i)
        driver.maximize_window()
        driver.implicitly_wait(10)
        test = Work(driver)
        test.login()
        sleep(2)
        test.click()
        sleep(2)
        handle = driver.window_handles[1]
        driver.switch_to.window(handle)
        driver.find_element_by_xpath("//span[text()='CPU']").click()
        sleep(2)
        # js = "document.getElementsByClassName('actionBox___3N6aR')[1].style='display:block;'"
        js = "document.getElementsByClassName('actionBox___3N6aR')[1].style.display='block'"
        # js = 'document.querySelectorAll("[class^=actionBox]")[1].style="display:block;"'
        driver.execute_script(js)
        sleep(2)
        driver.find_elements_by_xpath("//div[@class='actionBox___3N6aR']/img[@class='icon___1-22H']")[0].click()
