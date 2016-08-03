# FireMate
Implemented with Python 2.7.6

#Project prerequisites
pip install selenium
pip install pyvirtualdisplay
pip install py4j

#Run Configuration
Depending on the desired run options you will need to set the configs/RunOption.txt
Currently you may choose between dev, linux, windows as run configurations

#Package description
    Configs
        Contain run configurations that are picked up by the test framework and used to initialize the selenium driver
        correctly

    Data
        Contains test data. Each test has its initial data declared here. File naming matches the test user story number
        Ex US001.ini matches US001ViewPoliciesTest.py

    Drivers
        Currently contains chromedrivers for linux and windows

    External
        Contains an external jar. The jar contains ExtentReports (a reporting framework) and a wrapper that is build over it

    Pages
        First folder level in pages defines the website or webapplication that is mapped. the second level folders define the
        feature grouping of the pages.
        The actual page classes define web element mappings and actions that are defined for each feature

    Tests
        Tests are currently bundled under the test folder package. As the need will arise there will be changes in structure and
        tests will be grouped by features or some other structure.
        The actual test classes define the data that is used in the setup part of the test, the test flow and clean up actions
        in the tearDown part

    Tools
        This is a utility package.
            ConfigUtils - reads data from the Config package and is used by the DriverUtils class.
            DriverUtils - initializes the driver based on the provided Configs (ConfigUtils)
            FileUtils - reads data from the Data package. It is mostly used by the tests in the setUp part
            SoftAssert - defines a custom assertion class that enables multiple validation in a test before failing the test
            WebdriverBase - Defines the webdriver. it is extended by all page classes and is initialized by the DriverUtils class