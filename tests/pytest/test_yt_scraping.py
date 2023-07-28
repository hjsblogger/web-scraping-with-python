# Import the locators file
import sys
sys.path.append(sys.path[0] + "/..")
from pageobject.locators import locators
from pageobject.locators import *

from pageobject.helpers import helpers
from pageobject.helpers import *

@pytest.mark.usefixtures('driver')

class TestYoutubeScraping:
    def test_scrap_youtube(self, driver) -> list:
        meta_data_arr=[]
        driver.get(locators.test_yt_url)

        # Click on 'Accept All' in case the said window comes up
        # This occurs since cookies are cleared and machines are sanitized each run

        # Stack Overflow - https://stackoverflow.com/questions/66902404/selenium-python-click-agree-to-youtube-cookie
        # Locators were located using the below link
        # https://consent.youtube.com/m?continue=https%3A%2F%2Fwww.youtube.com%2F&gl=FR&m=0&pc=yt&uxe=23983172&hl=en&src=1

        # Below issue is not observed in local machines since there is no clean-up of cookies

        try:
            # Wait until the "Accept all" button is clickable
            accept_all = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "form:nth-child(3) > div > div > button[aria-label= 'Accept all']")))

            # Click the "Accept all" button
            accept_all.click()

            print("Click on Accept all successful")
        except Exception as e:
            # Even if this exception is raised, we can still continue test execution
            # This means that the button was not found & the YouTube channel link has opened successfully
            print(f"'Accept All' button not present, proceed with the tests: {str(e)}")

        meta_data_arr = helpers.scrap_yt_content(driver)
        helpers.print_scrapped_content(meta_data_arr)