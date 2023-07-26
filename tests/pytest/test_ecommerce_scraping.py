# Import the locators file
import sys
sys.path.append(sys.path[0] + "/../..")
from pageobject.locators import locators
from pageobject.locators import *

from pageobject.helpers import helpers
from pageobject.helpers import *

@pytest.mark.usefixtures('driver')

class TestEcommerceScrapping:
    def exemp_test_scrap_ecommerce(self, driver):
        driver.get(locators.test_ecomm_url)

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()

        # Commented once the tests are executed in non-headless mode
        # driver.maximize_window()

        # Create an instance of ActionChains
        actions = ActionChains(driver)

        # Explicit wait of 10 seconds
        wait = WebDriverWait(driver, 10)

        # Wait for the element to visible, it will be interactable once it is visible
        # element_cat = driver.find_element(By.XPATH, "//a[contains(.,'Shop by Category')]")
        element_cat = wait.until(EC.visibility_of_element_located((By.XPATH,
                locators.shopcategory)))

        # Move to the element and perform click operation
        actions.move_to_element(element_cat).click().perform()

        # element_category = driver.find_element(By.XPATH, "//span[contains(.,'Phone, Tablets & Ipod')]")
        element_phcat = wait.until(EC.visibility_of_element_located((By.XPATH,
                locators.phonecategory)))

        actions.move_to_element(element_phcat).click().perform()

        # Better to wait till the respective element is visible
        # Tough nut : 1 - nested locators!
        nested_elements = wait.until(EC.visibility_of_element_located((By.XPATH,
            "//div[@id='entry_212391']//div[@id='entry_212408']//div[@class='row']")))

        # Tough nut : 2 - nested locators!
        actual_items = nested_elements.find_elements(By.CLASS_NAME,
                "product-layout.product-grid.no-desc.col-xl-4.col-lg-4.col-md-4.col-sm-6.col-6")

        count = len(actual_items)
        # print("Number of elements found:" + str(count) + ".\n")

        meta_data_arr = []
        for ind_elem_props in actual_items:
            # nested_img_elem = ind_elem_props.find_element(By.CSS_SELECTOR,
            #    "div.product-thumb > div.product-thumb-top > div.image")
            
            ################ Product Image Link ################
            # item_image = nested_img_elem.find_element(By.XPATH,
            #    "//*[contains(@id, 'mz-product-grid-image')]")

            nested_product_name_elem = ind_elem_props.find_element(By.CSS_SELECTOR,
                "div.product-thumb > div.caption")
            
            ################ Product Name ################
            nested_title_elem = nested_product_name_elem.find_element(By.CSS_SELECTOR,
                    ".title .text-ellipsis-2")
            
            ################ Price #######################
            nested_price_elem = nested_product_name_elem.find_element(By.CSS_SELECTOR,
                    ".price .price-new")

            # Create a dictionary of the meta-data of the items on e-commerce store
            meta_data_dict = {
                'product image': nested_title_elem.get_attribute('href'),
                'product name': nested_title_elem.text,
                'product price': nested_price_elem.text
            }
            
            meta_data_arr.append(meta_data_dict)
    
        helpers.print_scrapped_content(meta_data_arr)

    def test_scrap_ecommerce(self, driver):
        meta_data_arr=[]
        driver.get(locators.test_ecomm_url)

        # Commented once the tests are executed in non-headless mode
        driver.maximize_window()

        # Create an instance of ActionChains
        # actions = ActionChains(driver)

        # Explicit wait of 10 seconds
        # wait = WebDriverWait(driver, 10)

        meta_data_arr = helpers.scrap_ecomm_content(driver)
        helpers.print_scrapped_content(meta_data_arr)