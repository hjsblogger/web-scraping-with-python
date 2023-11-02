# Selenium WebDriver used for infinite scrolling
# Beautiful Soup used for scraping content

#Beautiful Soup Official Documentation - https://www.crummy.com/software/BeautifulSoup/bs4/doc

import sys
# Import the locators file
import os
from pprint import pprint
sys.path.append(sys.path[0] + "/../..")

from pageobject.locators import locators
from pageobject.locators import *

from pageobject.helpers import helpers
from pageobject.helpers import *

exec_platform = os.getenv('EXEC_PLATFORM')

def scrap_inifite_website(url) -> list:
    meta_data_arr = []

    if exec_platform == 'cloud':
        username = environ.get('LT_USERNAME', None)
        access_key = environ.get('LT_ACCESS_KEY', None)

        gridURL = "https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
        
        ch_options = webdriver.ChromeOptions()
        ch_options.browser_version = "latest"
        ch_options.platform_name = "Windows 11"

        lt_options = {}
        lt_options["build"] = "Build: Web Scraping with Selenium & Beautiful Soup"
        lt_options["project"] = "Project: Web Scraping with Selenium & Beautiful Soup"
        lt_options["name"] = "Test: Web Scraping with Selenium & Beautiful Soup"

        lt_options["browserName"] = "Chrome"
        lt_options["browserVersion"] = "latest"
        lt_options["platformName"] = "Windows 11"

        lt_options["console"] = "error"
        lt_options["w3c"] = True
        lt_options["headless"] = True

        ch_options.set_capability('LT:Options', lt_options)

        driver = webdriver.Remote(
            command_executor = gridURL,
            options = ch_options
        )
    elif exec_platform == 'local':
        # Scroll through the entire page using Selenium
        options = ChromeOptions()

        # Refer https://www.selenium.dev/blog/2023/headless-is-going-away/ for the new way
        # to trigger browser in headless mode

        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)

    driver.get(url)

    # Took some support from https://stackoverflow.com/a/41181494/126105
    start_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        # Scroll to the bottom of the page
        driver.execute_script("window.scrollTo(0, " + str(start_height) + ")")
        # Wait for the content to load
        time.sleep(2)
        scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
        if (scroll_height == start_height):
            # If heights are the same, we reached the end of page
            break
        # print("scroll_height = " + str(scroll_height))
        time.sleep(2)
        start_height = scroll_height

    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, features='html.parser')
    
    # Instantiated Chrome instance is no longer required
    # since we have already read the source
    driver.quit()

    # Code changes as per 28/07/2023
    # In case if elements are not located, please change the locators accordingly
    rows = soup.find_all('div', class_='w-full rounded border post')
    print("\nTotal items on " + url + " are " + str(len(rows)) + "\n")

    for row in rows:
        dress = row.find('h4')
        link = dress.find('a')
        price = row.find('h5')
        

        # Create a dictionary of the meta-data of the items on e-commerce store
        meta_data_dict = {
            'dress': dress.text.strip(),
            'link' : link.get_attribute_list('href'),
            'price': price.text.strip()
        }
        
        meta_data_arr.append(meta_data_dict)
    return meta_data_arr

if __name__ == '__main__':
    meta_data_arr = scrap_inifite_website(locators.test_bs4_infinite_url)
    helpers.print_scrapped_content(meta_data_arr)
