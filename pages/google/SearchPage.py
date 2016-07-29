from tools.WebdriverBase import WebdriverBase

# Locators
searchInputLocator = "[name='q']"

class SearchPage(WebdriverBase):

    def input_search_term(self, searchTerm):
        # search
        searchInput = WebdriverBase().locate_element_by_css_selector(searchInputLocator)
        searchInput.send_keys(searchTerm)