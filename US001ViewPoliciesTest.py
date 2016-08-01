import unittest

from pages.hellfire.LoginPage import LoginPage
from pages.hellfire.navigation.NavigationMenuPage import NavigationMenuPage
from pages.hellfire.policies import PoliciesPage
from pages.hellfire.policies.PoliciesPage import PoliciesPage

baseURL = "https://www.google.com/ncr"
searchTerm = "darkside \n"


class US001ViewPoliciesTest(unittest.TestCase):
    def setUp(self):
        #login details
        self.userName = "admin"
        self.userPass = "admin"
        #menu selection
        # self.menuLabel = "Images"
        self.menuLabel = "Policies"

    def test_search(self):
        LoginPage().navigate_to("http://172.22.140.89:8014/login")
        # login actions
        LoginPage().perform_login(self.userName, self.userPass)
        NavigationMenuPage().click_on_menu_item(self.menuLabel)
        PoliciesPage().get_policies()
        PoliciesPage().get_policies_from("Workspace11")


    def tearDown(self):
        LoginPage().close_driver()
