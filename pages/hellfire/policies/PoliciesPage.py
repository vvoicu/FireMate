from tools import WebdriverBase
from tools.WebdriverBase import WebdriverBase

policiesContainerLocator = "div.index-tiles"


class PoliciesPage(WebdriverBase):
    def get_policies(self):
        policiesContainer = WebdriverBase().locate_element_by_css_selector(policiesContainerLocator)

        # policiesList = policiesContainer.locate_elements_by_css_selector("div.index-tiles__section header")
        policiesList = policiesContainer.find_elements_by_css_selector("div.index-tiles__section header")
        for itemNow in policiesList:
            print itemNow.text

    def get_policies_from(self, policiesName):

        policiesContainer = WebdriverBase().locate_element_by_css_selector(policiesContainerLocator)
        policiesList = policiesContainer.find_elements_by_css_selector("div.index-tiles__section")
        for itemNow in policiesList:
            if policiesName in itemNow.text:
                policiesWorkspaceNameList = itemNow.find_elements_by_css_selector("div.grommetux-tile strong")
                policiesWorkspaceDateList = itemNow.find_elements_by_css_selector("div.grommetux-tile div")

                for policiesItemNameNow in policiesWorkspaceNameList:
                    for policiesItemDateNow in policiesWorkspaceDateList:
                        policies = {}
                        policies['name']=policiesItemNameNow.text
                        policies['date']=policiesItemDateNow.text

    def print_policies(self, list):
        for itemNow
