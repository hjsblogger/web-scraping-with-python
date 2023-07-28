# Import the locators file
import sys
sys.path.append(sys.path[0] + "/../..")
from pageobject.locators import locators
from pageobject.locators import *

from pageobject.helpers import helpers
from pageobject.helpers import *

from pyunitsetup import pyunit_setup

test_setup = pyunit_setup()

def scrap_youtube(test_url) -> list:
    meta_data_arr=[]
    test_setup.setUp()
    test_setup.browser.get(test_url)

    # Click on 'Accept All' in case the said window comes up
    # This occurs since cookies are cleared and machines are sanitized each run

    # Stack Overflow - https://stackoverflow.com/questions/66902404/selenium-python-click-agree-to-youtube-cookie
    # Locators were located using the below link
    # https://consent.youtube.com/m?continue=https%3A%2F%2Fwww.youtube.com%2F&gl=FR&m=0&pc=yt&uxe=23983172&hl=en&src=1

    # Below issue is not observed in local machines since there is no clean-up of cookies

    try:
        # Wait until the "Accept all" button is clickable
        accept_all = WebDriverWait(test_setup.browser, 5).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "form:nth-child(3) > div > div > button[aria-label= 'Accept all']")))

        # Click the "Accept all" button
        accept_all.click()

        print("Click on Accept all successful")
    except Exception as e:
        # Even if this exception is raised, we can still continue test execution
        # This means that the button was not found & the YouTube channel link has opened successfully
        print(f"'Accept All' button not present, proceed with the tests: {str(e)}")

    meta_data_arr = helpers.scrap_yt_content(test_setup.browser)

    test_setup.tearDown()
    return meta_data_arr

def main():
    meta_data_arr = scrap_youtube(locators.test_yt_url)
    helpers.print_scrapped_content(meta_data_arr)

if __name__ == '__main__':
    main()