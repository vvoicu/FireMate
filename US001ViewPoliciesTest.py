import unittest

from pages.policies.LoginPage import LoginPage
from pages.policies.navigation.NavigationMenuPage import NavigationMenuPage

baseURL = "https://www.google.com/ncr"
searchTerm = "darkside \n"


class US001ViewPoliciesTest(unittest.TestCase):
    def setUp(self):
        #login details
        self.userName = "admin"
        self.userPass = "admin"
        #menu selection
        self.menuLabel = "Images"

    def test_search(self):
        LoginPage().navigate_to("http://172.22.140.89:8014/login")
        # login actions
        LoginPage().perform_login(self.userName, self.userPass)
        NavigationMenuPage().click_on_menu_item(self.menuLabel)

    def tearDown(self):
        LoginPage().close_driver()
