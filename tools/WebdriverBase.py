from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from DriverUtils import DriverUtils
from selenium import webdriver

## This headless configuration will work only on linux machines
##



class WebdriverBase(object):
    elementWait = 30
    driver = DriverUtils().start_driver()
    #config driver
    driver.maximize_window()
    driver.set_page_load_timeout(elementWait)

    def navigate_to(self, URL):
        self.driver.get(URL)

    def locate_element_by_css_selector(self, cssLocator):
        return WebDriverWait(self.driver, self.elementWait).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, cssLocator)))

    def locate_elements_by_css_selector(self, cssLocator):
        return WebDriverWait(self.driver, self.elementWait).until(
            EC.visibility_of_any_elements_located((By.CSS_SELECTOR, cssLocator)))

    def close_driver(self):
        self.driver.close()
        # self.driver.quit()