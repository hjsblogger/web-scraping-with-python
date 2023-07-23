# Import the locators file
import sys
sys.path.append(sys.path[0] + "/../..")
from pageobject.locators import locators
from pageobject.locators import *

from pageobject.helpers import helpers
from pageobject.helpers import *

from pyunitsetup import pyunit_setup

test_setup = pyunit_setup()

def scrap_ecommerce(test_url) -> list:
    # options = ChromeOptions()

    # Refer https://www.selenium.dev/blog/2023/headless-is-going-away/ for the new way
    # to trigger browser in headless mode

    # options.add_argument("--headless=new")
    # driver = webdriver.Chrome(options=options)
    # driver.get(test_url)

    test_setup.setUp()
    test_setup.browser.get(locators.test_ecomm_url)

    meta_data_arr=[]

    # Create an instance of ActionChains
    # actions = ActionChains(driver)

    # Explicit wait of 10 seconds
    # wait = WebDriverWait(driver, 10)

    meta_data_arr = helpers.scrap_ecomm_content(test_setup.browser)

    test_setup.tearDown()
    return meta_data_arr

def main():
    meta_data_arr = scrap_ecommerce(locators.test_ecomm_url)
    helpers.print_scrapped_content(meta_data_arr)

if __name__ == '__main__':
    main()