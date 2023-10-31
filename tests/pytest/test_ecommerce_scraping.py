# Import the locators file
import sys
sys.path.append(sys.path[0] + "/../..")
from pageobject.locators import locators
from pageobject.locators import *

from pageobject.helpers import helpers
from pageobject.helpers import *

@pytest.mark.usefixtures('driver')

class TestEcommerceScrapping:
    def test_scrap_ecommerce(self, driver):
        meta_data_arr=[]
        driver.get(locators.test_ecomm_url)

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()

        meta_data_arr = helpers.scrap_ecomm_content(driver)
        helpers.print_scrapped_content(meta_data_arr)