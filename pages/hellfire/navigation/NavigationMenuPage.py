from tools import WebdriverBase
from tools.WebdriverBase import WebdriverBase

navigationContainerLocator = "nav[class*='menu'] a"

class NavigationMenuPage(WebdriverBase):

    def click_on_menu_item(self, name):
        menuLinksList = WebdriverBase().locate_elements_by_css_selector(navigationContainerLocator)

        for itemNow in menuLinksList:
            print itemNow.text
            if itemNow.text == name:
                itemNow.click()
                print "Found it {} {}" .format(itemNow.text, name)
                break