from tools import WebdriverBase
from tools.WebdriverBase import WebdriverBase
from tools.FileUtils import FileUtils

policiesContainerLocator = "div.index-tiles"


class PoliciesPage(WebdriverBase):
    def get_policies_grouping_name(self):
        groupingList = []
        policiesContainer = WebdriverBase().locate_element_by_css_selector(policiesContainerLocator)
        policiesList = policiesContainer.find_elements_by_css_selector("div.index-tiles__section header")
        for itemNow in policiesList:
            groupingList.append(itemNow.text)
        return groupingList

    def get_policies_from_specific_policies_group(self, policiesName):
        list = []
        policiesContainer = WebdriverBase().locate_element_by_css_selector(policiesContainerLocator)
        policiesList = policiesContainer.find_elements_by_css_selector("div.index-tiles__section")
        for itemNow in policiesList:
            if policiesName in itemNow.text:
                policiesWorkspaceNameList = itemNow.find_elements_by_css_selector("div.grommetux-tile strong")
                policiesWorkspaceDateList = itemNow.find_elements_by_css_selector("div.grommetux-tile div")
                while (len(policiesWorkspaceNameList) != 0):
                    i = 0
                    policies = {}
                    policies['name'] = policiesWorkspaceNameList[i].text
                    policies['date'] = policiesWorkspaceDateList[i].text
                    list.append(policies)
                    policiesWorkspaceNameList.pop(i)
                    policiesWorkspaceDateList.pop(i)

        return list

    def get_policies_sorted_by_name(self):
        list = []
        policiesContainer = WebdriverBase().locate_element_by_css_selector(policiesContainerLocator)
        policiesList = policiesContainer.find_elements_by_css_selector("div.grommetux-tile--selectable")

        for itemNow in policiesList:
            policiesWorkspaceName = itemNow.find_element_by_css_selector("strong")
            policiesWorkspaceDate = itemNow.find_element_by_css_selector("div")
            policies = {}
            policies['name'] = policiesWorkspaceName.text
            policies['date'] = policiesWorkspaceDate.text
            list.append(policies)

        return list

    def print_policies(self, list):
        for itemNow in list:
            print itemNow
