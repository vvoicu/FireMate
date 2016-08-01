import unittest

from pages.hellfire.LoginPage import LoginPage
from pages.hellfire.navigation.NavigationMenuPage import NavigationMenuPage
from pages.hellfire.policies.PoliciesHeaderPage import PoliciesHeaderPage
from pages.hellfire.policies.FiltersPage import FiltersPage
from pages.hellfire.policies.PoliciesWorkspaceManagement import PoliciesWorkspaceManagement
from tools.WebdriverBase import WebdriverBase
from tools.DriverUtils import DriverUtils

baseURL = "http://172.22.140.89:8014/login"

class US003WorkspaceManagementTest(unittest.TestCase):
    def setUp(self):
        #login details
        self.userName = "admin"
        self.userPass = "admin"
        self.menuLabel = "Policies"

    def perform_test(self):
        LoginPage().navigate_to(baseURL)
        # login actions
        LoginPage().perform_login(self.userName, self.userPass)
        NavigationMenuPage().click_on_menu_item(self.menuLabel)
        PoliciesWorkspaceManagement().get_policies_management_button("Workspace11")