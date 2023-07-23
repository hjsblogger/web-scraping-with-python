# Import the locators file
import sys
from pageobject.locators import locators
from pageobject.locators import *

def create_actions(driver):
    actions = ActionChains(driver)
    return actions

def create_waits(driver, duration):
    # Explicit wait of 10 seconds
    wait = WebDriverWait(driver, duration)
    return wait

class helpers(object):
    def scrap_ecomm_content(driver)->list:
        meta_data_arr=[]
        # Explicit wait of 10 seconds
        wait = create_waits(driver, 10)

        actions = create_actions(driver)

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
        
        return meta_data_arr
    
    def print_scrapped_content(meta_data):
        for elem_info in meta_data:
            print(elem_info)