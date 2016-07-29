from tools.WebdriverBase import WebdriverBase

# Locators
listItemsLocator = "div.g"

class SearchListPage(WebdriverBase):

    def grab_search_results_list(self):
        # grab results list
        return WebdriverBase().locate_elements_by_css_selector(listItemsLocator)
