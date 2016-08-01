from tools import WebdriverBase
from tools.WebdriverBase import WebdriverBase

policiesContainerLocator = "div.index-tiles"


class PoliciesPage(WebdriverBase):
    def get_policies(self):
        policiesContainer = WebdriverBase().locate_element_by_css_selector(policiesContainerLocator)

        policiesList = policiesContainer.locate_elements_by_css_selector("div.index-tiles__section header")
        for itemNow in policiesList:
            print itemNow.text
