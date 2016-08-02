# from pyvirtualdisplay import Display
from selenium import webdriver
from ConfigUtils import ConfigUtils
import os

class DriverUtils(object):
    def start_linux_headless(self):
        # headless config
        # display = Display(visible=0, size=(800, 600))
        # display.start()
        pass

    def start_driver(self):

        configMap = ConfigUtils().read_config_file()

        if configMap["headlessMode"] == "true":
            self.start_linux_headless()

        if configMap["browser"] == "chrome":
            driverPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), configMap["chromePath"])
            driver = webdriver.Chrome(driverPath)

        if configMap["browser"] == "firefox":
            driver = webdriver.Firefox()

        return driver

