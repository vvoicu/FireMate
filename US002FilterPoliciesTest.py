import unittest

from pages.hellfire.LoginPage import LoginPage
from pages.hellfire.navigation.NavigationMenuPage import NavigationMenuPage
from pages.hellfire.policies.PoliciesHeaderPage import PoliciesHeaderPage
from pages.hellfire.policies.FiltersPage import FiltersPage

baseURL = "http://172.22.140.89:8014/login"

class US002FilterPoliciesTest(unittest.TestCase):
    def setUp(self):
        #login details
        self.userName = "admin"
        self.userPass = "admin"
        self.menuLabel = "Policies"
        self.sortType = "Name"
        self.policyName = "Workspace2"

    def test_search(self):
        LoginPage().navigate_to(baseURL)
        # login actions
        LoginPage().perform_login(self.userName, self.userPass)
        NavigationMenuPage().click_on_menu_item(self.menuLabel)
        PoliciesHeaderPage().click_filter_icon()
        FiltersPage().select_sort_type(self.sortType)

        FiltersPage().click_sort_descending()
        FiltersPage().click_sort_ascending()
        FiltersPage().grab_filters_list()
        FiltersPage().click_filter_policy(self.policyName)

    def tearDown(self):
        LoginPage().close_driver()