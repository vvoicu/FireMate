from tools import WebdriverBase
from tools.WebdriverBase import WebdriverBase

policiesContainerLocator = "div.index-tiles"

#managementButtonDictionary={}

class PoliciesWorkspaceManagement(WebdriverBase):
    def get_policies_management_button(self, workspacename):
        policiesContainer = WebdriverBase().locate_element_by_css_selector(policiesContainerLocator)

        # policiesList = policiesContainer.locate_elements_by_css_selector("div.index-tiles__section header")
        policiesList = policiesContainer.find_elements_by_css_selector("div.index-tiles__section header")
        policiesRightMenuButtons =policiesContainer.find_elements_by_css_selector("div")
        for i in len(policiesList):
            #managementButtonDictionary[policiesList[i]]=policiesRightMenuButtons[i]
            if(policiesList[i].text==workspacename):
                policiesRightMenuButtons[i].click()


