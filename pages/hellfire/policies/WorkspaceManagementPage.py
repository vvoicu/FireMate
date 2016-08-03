from tools import WebdriverBase
from tools.WebdriverBase import WebdriverBase
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, NoSuchWindowException
from tools.FileUtils import FileUtils
from tools.SoftAssert import SoftAssert

policiesContainerLocator = "div.index-tiles"
policiesButtonsContainer = "button+nav[role='menu']"

class WorkspaceManagementPage(WebdriverBase):
    def get_policies_management_button(self, workspacename):
        policiesContainer = WebdriverBase().locate_element_by_css_selector(policiesContainerLocator)
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

    def verify_the_displayed_management_buttons(self):
        buttonsList = WorkspaceManagementPage().get_buttons_grouping_name()
        print buttonsList
        buttonsToCompareList = FileUtils().read_properties_as_list("US003.ini", "managementButtons")
        print buttonsToCompareList
        SoftAssert().verfy_equals_true("not", buttonsList, buttonsToCompareList)
        print SoftAssert().failures_size()
        print SoftAssert().failures_list()


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



