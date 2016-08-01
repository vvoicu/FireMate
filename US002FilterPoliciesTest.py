import unittest

from pages.hellfire.LoginPage import LoginPage
from pages.hellfire.navigation.NavigationMenuPage import NavigationMenuPage
from pages.hellfire.policies.PoliciesHeaderPage import PoliciesHeaderPage

baseURL = "http://172.22.140.89:8014/login"
searchTerm = "darkside \n"


class US002FilterPoliciesTest(unittest.TestCase):
    def setUp(self):
        #login details
        self.userName = "admin"
        self.userPass = "admin"
        #menu selection
        self.menuLabel = "Policies"

    def test_search(self):
        LoginPage().navigate_to(baseURL)
        # login actions
        LoginPage().perform_login(self.userName, self.userPass)
        NavigationMenuPage().click_on_menu_item(self.menuLabel)
        PoliciesHeaderPage().click_filter_icon()

    def tearDown(self):
        LoginPage().close_driver()