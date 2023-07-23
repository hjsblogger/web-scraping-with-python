# Import the locators file
import sys
import os
from os import environ
sys.path.append(sys.path[0] + "/../..")
from pageobject.locators import locators
from pageobject.locators import *

exec_platform = os.getenv('EXEC_PLATFORM')

@pytest.fixture(scope='function')
def driver(request):
    if exec_platform == 'cloud':
        username = environ.get('LT_USERNAME', None)
        access_key = environ.get('LT_ACCESS_KEY', None)

        gridURL = "https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
        
        ch_options = webdriver.FirefoxOptions()
        ch_options.browser_version = "latest"
        ch_options.platform_name = "Windows 10"
        lt_options = {}
        lt_options["username"] = os.getenv("LT_USERNAME")
        lt_options["accessKey"] = os.getenv("LT_ACCESS_KEY")
        lt_options["build"] = "e-commerce and dropdown use cases"
        lt_options["project"] = "Elements Check Tests"
        lt_options["name"] = "E-commerce and dropdown tests"
        lt_options["console"] = "error"
        lt_options["w3c"] = True
        lt_options["headless"] = True
        lt_options["plugin"] = "python-python"

        ch_options.set_capability('LT:Options', lt_options)

        browser = webdriver.Remote(
            command_executor = gridURL,
            options = ch_options
        )

        yield browser

        def fin():
            # browser.execute_script("lambda-status=".format(str(not request.node.rep_call.failed if "passed" else
            # "failed").lower()))
            if request.node.rep_call.failed:
                browser.execute_script("lambda-status=failed")
            else:
                browser.execute_script("lambda-status=passed")
                browser.quit()

        request.addfinalizer(fin)
    elif exec_platform == 'local':
        options = ChromeOptions()

        # Refer https://www.selenium.dev/blog/2023/headless-is-going-away/ for the new way
        # to trigger browser in headless mode

        options.add_argument("--headless=new")
        browser = webdriver.Chrome()

        yield browser

        def fin():
            browser.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # this sets the result as a test attribute for LambdaTest reporting.
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)