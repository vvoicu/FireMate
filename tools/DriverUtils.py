from pyvirtualdisplay import Display
from selenium import webdriver
import os

class DriverUtils(object):
    def start_linux_headless(self):
        # headless config
        display = Display(visible=0, size=(800, 600))
        display.start()

    def start_driver(self):
        # self.start_linux_headless()
        return webdriver.Chrome("drivers/chromedriver")

    def read_run_config(self):
        pathRoot = os.getcwd().replace("tools","")
        with open(pathRoot + "configs/RunOption.txt", "r") as f:
            return f.readline()
        return "local2"

    def read_config_file(self):
        pass

if __name__ == "__main__":
    fineName = DriverUtils().read_run_config()
    print fineName
    # print os.getcwd().replace("tools")