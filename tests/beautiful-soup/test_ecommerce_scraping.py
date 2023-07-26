# Import the locators file
import sys
from pprint import pprint
sys.path.append(sys.path[0] + "/../..")

from pageobject.locators import locators
from pageobject.locators import *

from pageobject.helpers import helpers
from pageobject.helpers import *

def scrap_ecommerce(url) -> list:
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Unable to fetch the page. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())

    rows = soup.select('.product-layout.product-grid.no-desc.col-xl-4.col-lg-4.col-md-4.col-sm-6.col-6')
    # print(len(articles))

    meta_data_arr = []

    for row in rows:
        link = row.find("a", class_='carousel d-block slide')
        name = row.find("h4", class_='title')
        price = row.find("span", class_='price-new')

        # Create a dictionary of the meta-data of the items on e-commerce store
        meta_data_dict = {
            'product link': link.get_attribute_list('href'),
            'product name': name.get_text(),
            'product price': price.get_text()
        }
        
        meta_data_arr.append(meta_data_dict)
    return meta_data_arr

# Pagination - 1:5
# Page 1: https://ecommerce-playground.lambdatest.io/index.php?route=product/category&path=57&page=1
# Page 5: https://ecommerce-playground.lambdatest.io/index.php?route=product/category&path=57&page=5

for iteration in range(1,6):
    test_url = locators.test_bs4_url + "&page=" + str(iteration)
    meta_data_arr = scrap_ecommerce(test_url)
    print('\n')
    print("Product Page = " + test_url)
    print("*********************************************************************************************************\n")
    helpers.print_scrapped_content(meta_data_arr)