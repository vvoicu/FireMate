import unittest

from pages.hellfire.LoginPage import LoginPage
from pages.hellfire.navigation.NavigationMenuPage import NavigationMenuPage
from pages.hellfire.policies import WorkspaceManagementPage
from pages.hellfire.policies.WorkspaceManagementPage import WorkspaceManagementPage
from tools.FileUtils import FileUtils
from tools.SoftAssert import SoftAssert

workspaceName = "Workspace12"
manipulationButtonName = "Suspend"

class US003WorkspaceManagementTest(unittest.TestCase):
    def setUp(self):
        self.baseURL = FileUtils().read_property("US002.ini", "baseURL")
        self.userName = FileUtils().read_property("US002.ini", "userName")
        self.userPass = FileUtils().read_property("US002.ini", "userPass")
        self.menuLabel = FileUtils().read_property("US002.ini", "menuLabel")

    def test_US003WorkspaceManagementTest(self):
        LoginPage().navigate_to(self.baseURL)
        # login actions
        LoginPage().perform_login(self.userName, self.userPass)
        NavigationMenuPage().click_on_menu_item(self.menuLabel)
        WorkspaceManagementPage().get_policies_management_button(workspaceName)
        WorkspaceManagementPage().verify_the_displayed_management_buttons()
        WorkspaceManagementPage().choose_how_to_manage_your_workspace(manipulationButtonName)
        self.assertEqual(SoftAssert().failures_size(), 0, str(SoftAssert().failures_list()))

    def tearDown(self):
        LoginPage().close_driver()