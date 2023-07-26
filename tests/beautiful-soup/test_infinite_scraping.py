# Selenium WebDriver used for infinite scrolling
# Beautiful Soup used for scraping content

import sys
from pprint import pprint
sys.path.append(sys.path[0] + "/../..")

from pageobject.locators import locators
from pageobject.locators import *

from pageobject.helpers import helpers
from pageobject.helpers import *

def scrap_inifite_website(url) -> list:
    meta_data_arr = []
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

    # Why features='html.parser' is required
    # The code that caused this warning is on line 44 of the file <file>.
    # To get rid of this warning, pass the additional argument 'features="html.parser"'
    # to the BeautifulSoup constructor.
    soup = BeautifulSoup(driver.page_source, features='html.parser')
    # print(soup.prettify())
    
    # Instantiated Chrome instance is no longer required
    # since we have already read the source
    driver.quit()

    rows = soup.select('.col-lg-4.col-md-6.mb-4')
    print(len(rows))

    for row in rows:
        dress = row.find('h4', class_='card-title')
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