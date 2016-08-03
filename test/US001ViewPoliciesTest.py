import unittest

from pages.hellfire.LoginPage import LoginPage
from pages.hellfire.navigation.NavigationMenuPage import NavigationMenuPage
from pages.hellfire.policies import PoliciesPage
from pages.hellfire.policies.PoliciesPage import PoliciesPage
from pages.hellfire.policies.PoliciesHeaderPage import PoliciesHeaderPage
from pages.hellfire.policies.FiltersPage import FiltersPage
from tools.SoftAssert import SoftAssert
from tools.FileUtils import FileUtils
import logging


logging.basicConfig(filename = "US001ViewPoliciesTest.log", level = logging.INFO)
class US001ViewPoliciesTest(unittest.TestCase):
    def setUp(self):
        # test data
        self.policiesFileName = "US001.ini"
        self.baseURL = FileUtils().read_property("US001.ini", "baseURL")
        self.userName = FileUtils().read_property("US001.ini", "userName")
        self.userPass = FileUtils().read_property("US001.ini", "userPass")
        self.menuLabel = FileUtils().read_property("US001.ini", "menuLabel")
        self.sortType = FileUtils().read_property("US001.ini", "sortType")
        self.policiesGroupName = FileUtils().read_property("US001.ini", "policiesGroupName")
        self.allPoliciesGroupingNameList = "allPoliciesGroupingNameList"
        self.policiesByGroupList = "policiesByGroupList"
        self.allPoliciesList = "allPoliciesList"

    def test_search(self):
        LoginPage().navigate_to(self.baseURL)
        # login actions
        LoginPage().perform_login(self.userName, self.userPass)
        NavigationMenuPage().click_on_menu_item(self.menuLabel)

        listAplicationPoliciesGrouping = PoliciesPage().get_policies_grouping_name()
        listAplicationPoliciesBySpecificGrouping = PoliciesPage().get_policies_from_specific_policies_group(
            self.policiesGroupName)

        listFilePoliciesGrouping = FileUtils().read_properties_as_list(self.policiesFileName,
                                                                       self.allPoliciesGroupingNameList)
        listFilePoliciesBySpecificGrouping = FileUtils().read_properties_as_dictionary(self.policiesFileName,
                                                                                       self.policiesByGroupList)
        listFileAllPolicies = FileUtils().read_properties_as_dictionary(self.policiesFileName, self.allPoliciesList)

        # verify that aplication contains all the policies grouping specified in the file
        SoftAssert().verfy_equals_true("List of policies grouping name doesn't matched ",
                                       listAplicationPoliciesGrouping, listFilePoliciesGrouping)
        # verify that aplication contains all the policies from a specified groupin policies given from file
        SoftAssert().verfy_equals_true("List of policies from specific group doesn't matched  ",
                                       listAplicationPoliciesBySpecificGrouping,
                                       listFilePoliciesBySpecificGrouping)

        PoliciesHeaderPage().click_filter_icon()
        FiltersPage().select_sort_type(self.sortType)
        listAplicationAllPolicies = PoliciesPage().get_policies_sorted_by_name()
        # verify that aplication contains all the policies when sorting by name is selected
        SoftAssert().verfy_equals_true("List of all policies doesn't matched", listAplicationAllPolicies,
                                       listFileAllPolicies)

        print SoftAssert().failures_size()
        print SoftAssert().failures_list()
        self.assertEqual(SoftAssert().failures_size(), 0, str(SoftAssert().failures_list()))

    def tearDown(self):
        LoginPage().close_driver()
