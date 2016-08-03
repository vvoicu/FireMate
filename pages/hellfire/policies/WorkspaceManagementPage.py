from tools import WebdriverBase
from tools.WebdriverBase import WebdriverBase
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, NoSuchWindowException
from tools.FileUtils import FileUtils
from tools.SoftAssert import SoftAssert
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

policiesContainerLocator = "div.index-tiles"
policiesButtonsContainer = "button+nav[role='menu']"

class WorkspaceManagementPage(WebdriverBase):
    def get_policies_management_button(self, workspacename):
        policiesContainer = WebdriverBase().locate_element_by_css_selector(policiesContainerLocator)

        # policiesList = policiesContainer.locate_elements_by_css_selector("div.index-tiles__section header")
        policiesList = policiesContainer.find_elements_by_css_selector("div.index-tiles__section header")
        for elementNow in policiesList:
            if (elementNow.text == workspacename):
                policiesRightMenuButton = elementNow.find_element_by_css_selector("div.index-tiles__section header div")
                policiesRightMenuButton.click()
                break

    def get_buttons_grouping_name(self):
        allButtonsList = []
        buttonsContainer = WebdriverBase().locate_element_by_css_selector(policiesButtonsContainer)
        if buttonsContainer.is_displayed():
            buttonsList = buttonsContainer.find_elements_by_css_selector("a")
            for itemNow in buttonsList:
                allButtonsList.append(itemNow.text)
            return allButtonsList

    def choose_how_to_manage_your_workspace(self, manipulationButton):
        buttonsContainer = WebdriverBase().locate_element_by_css_selector(policiesButtonsContainer)
        try:
            if buttonsContainer.is_displayed():
                buttonsList = buttonsContainer.find_elements_by_css_selector("a")
                for buttonNow in buttonsList:
                    if buttonNow.text == manipulationButton:
                        buttonNow.click()
                        break
        except StaleElementReferenceException as e:
            print (e)

    # def verify_the_buttons_list(self):
    #     buttonsContainer = WebdriverBase().locate_element_by_css_selector(policiesButtonsContainer)
    #     buttonsList = buttonsContainer.find_elements_by_css_selector("a")
    #     buttonsListToCompare = FileUtils().read_properties_as_list("US003.ini", "managementButtons")
    #     SoftAssert().verfy_equals_true("not", buttonsList, buttonsListToCompare)
    #     print SoftAssert().failures_size()
    #     print SoftAssert().failures_list()
    #     print buttonsList
    #     print buttonsListToCompare
        # unittest.assertListEqual(buttonsList, buttonsListToCompare, msg=None)



