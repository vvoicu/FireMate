from tools import WebdriverBase
from tools.WebdriverBase import WebdriverBase
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, NoSuchWindowException

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

    def choose_how_to_manage_your_workspace(self, manipulationButton):
        try:
            buttonsContainer = WebdriverBase().locate_element_by_css_selector(policiesButtonsContainer)
            if buttonsContainer.is_displayed():
                buttonsList = buttonsContainer.find_elements_by_css_selector("a")
                for buttonNow in buttonsList:
                    if buttonNow.text == manipulationButton:
                        buttonNow.click()
                        break
        except StaleElementReferenceException as e:
            print (e)
