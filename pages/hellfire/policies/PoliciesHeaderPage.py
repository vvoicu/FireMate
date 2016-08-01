from tools import WebdriverBase
from tools.WebdriverBase import WebdriverBase

#locators
headerLocator = "header[class*='index']"
filterIconLocator = "button[aria-label*='Filter']"

class PoliciesHeaderPage(WebdriverBase):
    def click_filter_icon(self):
        filterIconButton = self.locate_element_by_css_selector(filterIconLocator)
        filterIconButton.click()