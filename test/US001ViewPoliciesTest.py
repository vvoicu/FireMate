import unittest

from pages.hellfire.LoginPage import LoginPage
from pages.hellfire.navigation.NavigationMenuPage import NavigationMenuPage
from pages.hellfire.policies import PoliciesPage
from pages.hellfire.policies.PoliciesPage import PoliciesPage
from pages.hellfire.policies.PoliciesHeaderPage import PoliciesHeaderPage
from pages.hellfire.policies.FiltersPage import FiltersPage
from tools.SoftAssert import SoftAssert
from tools.FileUtils import FileUtils

baseURL = "https://www.google.com/ncr"
searchTerm = "darkside \n"


class US001ViewPoliciesTest(unittest.TestCase):
    def setUp(self):
        # login details
        self.userName = "admin"
        self.userPass = "admin"
        # menu selection
        # self.menuLabel = "Images"
        self.menuLabel = "Policies"
        self.sortType = "Name"

    def test_search(self):
        LoginPage().navigate_to("http://172.22.140.89:8014/login")
        # login actions
        LoginPage().perform_login(self.userName, self.userPass)
        NavigationMenuPage().click_on_menu_item(self.menuLabel)

        listAplicationGrouping = PoliciesPage().get_policies_grouping_name()
        print listAplicationGrouping

        listPoliciesGrouping = PoliciesPage().get_policies_sorted_by_type("Workspace11")
        # PoliciesPage().print_policies(list)
        # PoliciesHeaderPage().click_filter_icon()
        # FiltersPage().select_sort_type(self.sortType)
        # listName = PoliciesPage().get_policies_sorted_by_name()
        # PoliciesPage().print_policies(listName)

        fileGrouping = FileUtils().read_properties_as_list("policies.ini", "grouping")
        fileGroupingName = FileUtils().read_properties_as_list("policies.ini", "Workspace11")
        print fileGrouping
        print fileGroupingName
        print listPoliciesGrouping


        # SoftAssert().verfy_equals_true("not", listPoliciesGrouping, fileGroupingName)
        SoftAssert().verfy_equals_true("not", listAplicationGrouping, fileGrouping)
        print SoftAssert().failures_size()
        print SoftAssert().failures_list()

        self.assertEqual(SoftAssert().failures_size(), 0, str(SoftAssert().failures_list()))


    def tearDown(self):
        LoginPage().close_driver()
