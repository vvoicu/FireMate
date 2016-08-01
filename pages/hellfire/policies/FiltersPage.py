from tools.WebdriverBase import WebdriverBase
from selenium.webdriver.support.ui import Select

filterContainerLocator = "div[class*='index-filters']"
sortSelectLocator = "select.flex"
sortButtonListLocators = "span > button"

policyTypeListLocator = "h3 + div[class*='column'] label"

class FiltersPage(WebdriverBase):
    def grab_filters_list(self):
        policyTypes = WebdriverBase().locate_elements_by_css_selector(policyTypeListLocator)
        for itemNow in policyTypes:
            print itemNow.text
        return policyTypes

    def click_filter_policy(self, policyName):
        policyTypes = WebdriverBase().locate_elements_by_css_selector(policyTypeListLocator)
        for itemNow in policyTypes:
            if policyName == itemNow.text:
                itemNow.click()
                print "found it.... the policy"
                break

    def select_sort_type(self, sortType):
        select = Select(WebdriverBase().locate_element_by_css_selector(sortSelectLocator))
        select.select_by_visible_text(sortType)

    def click_sort_ascending(self):
        WebdriverBase().locate_elements_by_css_selector(sortButtonListLocators)[0].click()

    def click_sort_descending(self):
        WebdriverBase().locate_elements_by_css_selector(sortButtonListLocators)[1].click()
