import unittest

from pages.google.SearchListPage import SearchListPage
from pages.google.SearchPage import SearchPage

baseURL = "https://www.google.com/ncr"
searchTerm = "darkside \n"

class GoogleSearch(unittest.TestCase):

    def test_search(self):
        # test actions
        SearchPage().navigate_to(baseURL)

        # search
        SearchPage().input_search_term(searchTerm)
        searchList = SearchListPage().grab_search_results_list()

        # print all results text
        for i in range(0, len(searchList)):
            a = searchList[i].text
            print "item: " + a

    def tearDown(self):
        # printScreenName = "FileOna.png"
        # self.driver.get_screenshot_as_file(printScreenName)
        SearchPage().close_driver()
