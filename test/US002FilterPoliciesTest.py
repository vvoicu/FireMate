import unittest

from pages.hellfire.LoginPage import LoginPage
from pages.hellfire.navigation.NavigationMenuPage import NavigationMenuPage
from pages.hellfire.policies.PoliciesHeaderPage import PoliciesHeaderPage
from pages.hellfire.policies.FiltersPage import FiltersPage
from tools.FileUtils import FileUtils



class US002FilterPoliciesTest(unittest.TestCase):
    def setUp(self):
        #test data
        self.baseURL = FileUtils().read_property("US002.ini", "baseURL")
        self.userName = FileUtils().read_property("US002.ini", "userName")
        self.userPass = FileUtils().read_property("US002.ini", "userPass")
        self.menuLabel = FileUtils().read_property("US002.ini", "menuLabel")
        self.sortType = FileUtils().read_property("US002.ini", "sortType")
        self.policyName = FileUtils().read_property("US002.ini", "policyName")

    def test_search(self):
        LoginPage().navigate_to(self.baseURL)
        # login actions
        LoginPage().perform_login(self.userName, self.userPass)
        NavigationMenuPage().click_on_menu_item(self.menuLabel)
        PoliciesHeaderPage().click_filter_icon()
        FiltersPage().select_sort_type(self.sortType)

        FiltersPage().click_sort_descending()
        FiltersPage().click_sort_ascending()
        print FiltersPage().grab_filters_list()
        FiltersPage().click_filter_policy(self.policyName)

    def tearDown(self):
        LoginPage().close_driver()