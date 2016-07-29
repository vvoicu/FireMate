import unittest

from pages.policies.LoginPage import LoginPage
from pages.policies.navigation.NavigationMenuPage import NavigationMenuPage

baseURL = "https://www.google.com/ncr"
searchTerm = "darkside \n"

class US001ViewPoliciesTest(unittest.TestCase):

    def setUp(self):
        pass


    def test_search(self):
        LoginPage().navigate_to("http://172.22.140.89:8014/login")
        # login actions
        LoginPage().input_user_name("admin")
        LoginPage().input_user_pass("admin")

        LoginPage().click_login_button()

        NavigationMenuPage().click_on_menu_item("Images")


    def tearDown(self):
        LoginPage().close_driver()